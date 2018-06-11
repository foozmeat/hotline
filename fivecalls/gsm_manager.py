import platform
import time
from random import choice

import serial

from fivecalls.singleton import Singleton


class GSMManager(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.connection = None
        self.eol = '\r\n'
        self.port = '/dev/serial0'
        self.volume = 0
        self.status = 0

        if platform.system() == 'Darwin':
            self.port = '/dev/tty.usbserial'

    def power_on(self):

        # possibly check a power status pin?

        if platform.system() == 'Darwin':
            return

    def power_off(self):

        if platform.system() == 'Darwin':
            return

    def open(self) -> bool:

        if self.connection and self.connection.is_open:
            return True

        self.power_on()

        try:
            self.connection = serial.Serial(
                    self.port,
                    115200,
                    timeout=0.2,
            )
        except serial.serialutil.SerialException:
            raise

        else:
            self.write('AT')
            result = self.flush().strip()
            self.send_at_cmd('+CHFA=1')  # Select AUX out

            if result != 'OK':
                print(f"Unable to open serial connection: {result}")
                return False

            self.get_volume()
            self.get_phone_status()
            return True

    def is_open(self) -> bool:
        return self.connection and self.connection.is_open

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            self.power_off()

    def write(self, cmd):
        cmd = bytes(cmd + self.eol, 'ascii')
        print(f"WRITE-> {cmd}")
        self.connection.write(cmd)
        self.readline(decode=False)

    def readline(self, decode=True) -> str:

        data = self.connection.readline().strip()
        print(f"READ -> {data}")

        if decode:
            data_str = data.decode('ascii')  # type: str
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

        cmd = 'AT' + cmd
        self.write(cmd)

        result = self.readline().strip()
        self.flush()

        return result

    def send_cmd_and_wait(self, cmd: str, wait_for: str):
        if not self.is_open():
            return ""

        cmd = 'AT' + cmd
        self.write(cmd)

        found = False
        data = ''

        while not found:
            data += self.flush()
            if wait_for in data:
                found = True

        return data

    def _get_numeric_result(self, cmd):
        r = self.send_at_cmd(cmd)

        if 'ERROR' in r:
            return 0

        _, val = r.split(' ')

        try:
            return int(val)
        except ValueError:
            return 0

    def get_volume(self):
        self.volume = self._get_numeric_result('+CLVL?')
        print(f"Volume: {self.volume}")

    def set_volume(self, new_vol: int):
        print(f"Setting volume to {new_vol}")
        r = self.send_at_cmd(f'+CLVL={new_vol}')
        self.get_volume()

    def hang_up(self):
        self.send_at_cmd('H')

    def dial_number(self, number: str):

        n_list = list(number)
        tones = ','.join(n_list)

        self.send_cmd_and_wait(f'+STTONE=1,20,2000', '+STTONE: 0')
        self.send_at_cmd(f'+CLDTMF=1,"{tones}",80')

        self.send_at_cmd(f"D{number};")

    def get_phone_status(self):
        self.status = self._get_numeric_result('+CPAS')
        print(f"Status: {self.status}")


if __name__ == '__main__':
    g = GSMManager()
    g.open()
    g.set_volume(100)
    # g.set_volume(choice(range(0, 100)))
    g.dial_number('5038163008')
    g.get_phone_status()
    while g.status != 0:
        g.get_phone_status()
        time.sleep(0.5)
    g.close()
