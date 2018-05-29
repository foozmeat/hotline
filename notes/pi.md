* screen rotation - add `display_rotate=3` to `/boot/config.txt`
* screen brightness `echo 255 > /sys/class/backlight/rpi_backlight/brightness`
* disable HDMI - `tvservice -o`
* video memory split needs to be 256
* `~/.kivy/config.ini` input provider should be `pitft = mtdev,/dev/input/event2,rotation=270`
