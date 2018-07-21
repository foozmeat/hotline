#!/bin/sh

set -u
set -e

# Install hotline
rsync -av --exclude ansible --exclude buildroot --exclude __pycache__ \
--exclude .git* --exclude .idea --exclude .DS_Store \
--delete \
/opt/hotline/ ${TARGET_DIR}/opt/hotline/
