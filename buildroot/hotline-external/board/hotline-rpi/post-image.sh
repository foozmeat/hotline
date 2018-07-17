#!/bin/bash

set -ex

BOARD_DIR="$(dirname $0)"
BOARD_NAME="$(basename ${BOARD_DIR})"
GENIMAGE_CFG="${BOARD_DIR}/genimage-${BOARD_NAME}.cfg"
GENIMAGE_TMP="${BUILD_DIR}/genimage.tmp"

cp ${BR2_EXTERNAL_HOTLINE_PATH}/board/${BOARD_NAME}/config.txt ${BINARIES_DIR}/config.txt
cp ${BR2_EXTERNAL_HOTLINE_PATH}/board/${BOARD_NAME}/cmdline.txt ${BINARIES_DIR}/cmdline.txt

rm -rf "${GENIMAGE_TMP}"

genimage                           \
	--rootpath "${TARGET_DIR}"     \
	--tmppath "${GENIMAGE_TMP}"    \
	--inputpath "${BINARIES_DIR}"  \
	--outputpath "${BINARIES_DIR}" \
	--config "${GENIMAGE_CFG}"

exit $?
