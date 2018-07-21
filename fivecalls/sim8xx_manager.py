import subprocess
import sys
import re
import time
from pathlib import Path

import serial
from fivecalls.singleton import Singleton

LINUX = False
if sys.platform == 'linux':
    import RPi.GPIO as GPIO

    LINUX = True


class SIM8XXManager(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.connection = None
        self.eol = '\r\n'
        self.port = '/dev/serial0'
        self.volume = 0
        self.status = 0

        if not LINUX:
            self.port = '/dev/tty.usbserial'

    def toggle_power(self):

        if not LINUX:
            return
        else:
            print("Toggling Power")
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4, GPIO.LOW)
            time.sleep(1)
            GPIO.output(4, GPIO.HIGH)
            GPIO.cleanup()

    def open(self) -> bool:

        if self.is_open():
            return True

        try:
            self.connection = serial.Serial(
                    self.port,
                    115200,
                    timeout=0.2,
            )
        except serial.serialutil.SerialException:
            raise

        else:
            if not self.is_powered_on():
                self.toggle_power()
                time.sleep(3)

            if not self.is_powered_on():
                print(f"Unable to open serial connection")
                return False

            # if not LINUX:
            self.send_at_cmd('AT+CHFA=1')  # Select AUX out

            self.send_at_cmd('AT+CMEE=2')  # Enable verbose errors
            self.set_volume(100)
            self.get_volume()
            self.get_phone_status()
            return True

    def is_powered_on(self) -> bool:
        if not self.is_open():
            return False

        self.write('AT')
        result = self.flush().strip()
        return "OK" in result

    def is_open(self) -> bool:
        return self.connection and self.connection.is_open

    def close(self):
        if self.connection and self.connection.is_open:
            print("Closing serial connection")
            self.connection.close()
            self.toggle_power()

    def write(self, cmd):
        print(f"WRITE-> {cmd}")
        cmd = bytes(cmd + self.eol, 'ascii')
        self.connection.write(cmd)
        self.connection.readline()

    def readline(self, decode=True) -> str:

        data = self.connection.readline().strip()

        if decode:
            data_str = data.decode('ascii')  # type: str
            print(f"READ -> {data_str}")
            return data_str
        else:
            return ""

    def flush(self, chunk_size=128, max_size=1024 * 1024) -> str:

        buffer = b""

        if self.connection:

            while True:
                byte_chunk = self.connection.read(size=chunk_size)
                buffer += byte_chunk
                if not len(byte_chunk) == chunk_size:
                    break

                if len(buffer) >= max_size:
                    break

        try:
            decoded = buffer.decode('ascii')
            return decoded
        except UnicodeDecodeError:
            return ""

    def send_at_cmd(self, cmd: str) -> str:

        if not self.is_open():
            return ""

        self.write(cmd)

        result = self.readline().strip()
        self.flush()

        return result

    def send_cmd_and_wait(self, cmd: str, wait_for: str):
        if not self.is_open():
            return ""

        self.write(cmd)

        found = False
        data = ''

        while not found:
            data += self.flush()
            if wait_for in data:
                found = True

        print(f"READ -> {data}")
        return data

    def _get_numeric_result(self, cmd):
        r = self.send_at_cmd(cmd)

        if 'ERROR' in r:
            return 0

        try:
            _, val = r.split(' ')

            return int(val)
        except ValueError:
            return 0

    def get_volume(self):
        self.volume = self._get_numeric_result('AT+CLVL?')
        print(f"Volume: {self.volume}")

    def set_volume(self, new_vol: int):
        print(f"Setting volume to {new_vol}")
        r = self.send_at_cmd(f'AT+CLVL={new_vol}')
        self.get_volume()

    def hang_up(self):
        self.send_at_cmd('ATH')

    def dial_number(self, number: str):

        if not self.open():
            return

        n_list = list(number)
        tones = ','.join(n_list)

        self.send_cmd_and_wait(f'AT+STTONE=1,20,2000', '+STTONE: 0')
        self.send_at_cmd(f'AT+CLDTMF=1,"{tones}",80')

        self.send_at_cmd(f"ATD{number};")

    def get_phone_status(self):
        self.status = self._get_numeric_result('AT+CPAS')
        print(f"Status: {self.status}")

    # def _gprs_connected(self) -> bool:
    #     result = self.send_at_cmd('AT+SAPBR=2,1')
    #     m = re.search(r'\+SAPBR: 1,(\d),"[0-9\.]+"', result)
    #     status_code = m.group(1)
    #     return status_code == "1"

    # def _open_gprs(self):
    #
    #     if not self.open():
    #         return
    #
    #     if not self._gprs_connected():
    #         self.send_cmd_and_wait(f'AT+SAPBR=3,1,"Contype","GPRS"', 'OK')
    #         self.send_cmd_and_wait(f'AT+SAPBR=3,1,"APN","CMNET"', 'OK')
    #         self.send_cmd_and_wait(f'AT+SAPBR=1,1', 'OK')

    # def _close_gprs(self):
    #     self.send_cmd_and_wait(f'AT+SAPBR=0,1', 'OK')

    def _ppp_is_up(self) -> bool:
        ppp_interface = Path('/sys/class/net/ppp0')
        return ppp_interface.exists()

    def ppp_up(self) -> bool:

        if self._ppp_is_up():
            return True

        if not self.open():
            return False

        print("Bringing ppp0 up")
        if self.connection:
            self.connection.close()

        subprocess.call(['/usr/bin/pon', 'sim8xx'])
        timeout = 0

        while not self._ppp_is_up():
            time.sleep(1)
            timeout += 1

            if timeout >= 10:
                return False

        return True

    def ppp_down(self) -> bool:
        if not self._ppp_is_up():
            return True

        print("Tearing ppp0 down")
        subprocess.call(['/usr/bin/poff', 'sim8xx'])
        return True

    # def http_get(self, url):
    #
    #     self._open_gprs()
    #     # self.send_at_cmd(f'AT+HTTPTERM')  # In case we're in a stale context
    #     self.send_cmd_and_wait(f'AT+HTTPINIT', 'OK')
    #     self.send_cmd_and_wait(f'AT+HTTPPARA="CID",1', 'OK')
    #     self.send_cmd_and_wait(f'AT+HTTPPARA="REDIR",1', 'OK')
    #     # self.send_cmd_and_wait(f'AT+HTTPPARA="URL","{url}"', 'OK')
    #     self.send_cmd_and_wait(f'AT+HTTPPARA="URL","ifconfig.co/ip"', 'OK')
    #
    #     self.send_cmd_and_wait(f'AT+HTTPSSL=1', 'OK')  # Not supported by all SIM8xx chips
    #     self.send_cmd_and_wait(f'AT+HTTPACTION=0', '+HTTPACTION: 0')
    #
    #     self.write('AT+HTTPREAD')
    #     result = self.readline()
    #     data = ""
    #     m = re.search(r'\+HTTPREAD: (\d+)', result)
    #     if m:
    #         length = int(m.group(1))
    #
    #         data = self.flush()
    #         data = data[0:length]
    #
    #     self.send_cmd_and_wait(f'AT+HTTPTERM', 'OK')
    #     # self._close_gprs()
    #
    #     return data


if __name__ == '__main__':
    from random import choice

    g = SIM8XXManager()
    # g.open()

    # g.set_volume(100)
    # g.set_volume(choice(range(0, 100)))
    g.dial_number('5038163008')
    g.get_phone_status()
    while g.status != 0:
        g.get_phone_status()
        time.sleep(0.5)

    # print(g.http_get('ifconfig.co/ip'))

    g.close()
