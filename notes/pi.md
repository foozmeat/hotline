# OS Setup
* screen rotation - add `display_rotate=3` to `/boot/config.txt`
* screen brightness `echo 255 > /sys/class/backlight/rpi_backlight/brightness`
* disable HDMI - `tvservice -o`
* video memory split needs to be 256

* speed up boot
```
systemd-analyze blame

systemctl disable apt-daily.service
systemctl disable apt-daily.timer
systemctl disable apt-daily-upgrade.timer
systemctl disable apt-daily-upgrade.service

apt remove triggerhappy avahi-daemon bluez dbus rpcbind
```

* For headless setup, SSH can be enabled by placing a file named 'ssh', without any extension, onto the boot partition of the SD card.
* Raspbian, since May 2016, checks the contents of the boot directory for a file called wpa_supplicant.conf, and will copy the file into /etc/wpa_supplicant, replacing any existing wpa_supplicant.conf file that may be there.

## Setting up the app environment

```
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev libmtdev1
```

* Install Python 3.6 from source into `/opt/python3.6`

```
sudo /opt/python3.6/bin/pip3.6 install pipenv
/opt/python3.6/bin/pipenv --python /opt/python3.6/bin/python3.6 install
```

* PPP configuration
  * `apt install ppp`
  * `usermod -G dip -a pi`
  * install peer script in `/etc/ppp/peers/sim8xx`
```
connect "/usr/sbin/chat -v -f /etc/chatscripts/gprs -T wholesale"
/dev/ttyAMA0
115200
noipdefault
usepeerdns
defaultroute
persist
noauth
nocrtscts
local
```
  * `pon sim8xx` brings up the interface
  * `poff sim8xx` tears it down

* TFT backlight
  * `echo 1 > /sys/class/backlight/rpi_backlight/bl_power` # OFF
  * `echo 0 > /sys/class/backlight/rpi_backlight/bl_power` # ON
