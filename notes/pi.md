* screen rotation - add `display_rotate=3` to `/boot/config.txt`
* screen brightness `echo 255 > /sys/class/backlight/rpi_backlight/brightness`
* disable HDMI - `tvservice -o`
* video memory split needs to be 256
* packages to remove `triggerhappy avahi-daemon bluez dbus rpcbind dhcpcd5 luajit`
