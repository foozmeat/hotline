#!/bin/sh

export BR2_DL_DIR=${HOME}/dl
export BR2_EXTERNAL=/opt/hotline/buildroot/hotline-external

make hotline-rpi2_defconfig
