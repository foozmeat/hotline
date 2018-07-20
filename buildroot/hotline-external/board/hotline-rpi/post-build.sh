#!/bin/sh

set -u
set -e

# Install hotline
rsync -av --exclude ansible --exclude buildroot --exclude __pycache__ \
--exclude .git* --exclude .idea --exclude .DS_Store \
--delete \
/opt/hotline/ ${TARGET_DIR}/opt/hotline/

# Add a console on tty1
if [ -e ${TARGET_DIR}/etc/inittab ]; then
    grep -qE '^tty1::' ${TARGET_DIR}/etc/inittab || \
	sed -i '/GENERIC_SERIAL/a\
tty1::respawn:/sbin/getty -L  tty1 0 vt100 # HDMI console' ${TARGET_DIR}/etc/inittab
fi
