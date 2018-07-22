#!/bin/sh

/usr/sbin/chat -f /opt/time/powered_on.chat -t 1 > /dev/ttyAMA0 < /dev/ttyAMA0

if [ $? != 0 ]; then
  echo "Powering up modem"

  echo 4 > /sys/class/gpio/export
  echo out > /sys/class/gpio/gpio4/direction
  echo 0 > /sys/class/gpio/gpio4/value
  sleep 1
  echo 1 > /sys/class/gpio/gpio4/value
  sleep 3

  chat -f /opt/time/powered_on.chat -t 1 > /dev/ttyAMA0 < /dev/ttyAMA0

  if [ $? != 0 ]; then
    echo "Modem still didn't wake up"
    exit 1
  fi

else
  echo "Modem is awake"
fi

RESULT=$( { chat -f /opt/time/get_time.chat -t 4 > /dev/ttyAMA0 < /dev/ttyAMA0; } 2>&1)
RESULT=$(echo $RESULT | sed -r 's/.*\+CCLK: "//') # strip head
RESULT=$(echo $RESULT | sed -r 's/-[[:digit:]]+"$//') # strip tail
RESULT=$(echo $RESULT | sed -r 's/,/ /') # date hates commas
RESULT=20${RESULT} # whole year to make date happy

date -s "${RESULT}" '+%Y/%m/%d %T' > /dev/null
