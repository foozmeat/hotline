################################################################################
#
# python-kivy
#
################################################################################

PYTHON_KIVY_VERSION = 1.10.1
PYTHON_KIVY_SITE = $(call github,kivy,kivy,$(PYTHON_KIVY_VERSION))
PYTHON_KIVY_SETUP_TYPE = distutils
PYTHON_KIVY_LICENSE = MIT
PYTHON_KIVY_LICENSE_FILES = LICENSE
PYTHON_KIVY_DEPENDENCIES = host-python-cython-hotline rpi-userland

PYTHON_KIVY_ENV += KIVY_CROSS_PLATFORM=rpi
PYTHON_KIVY_ENV += KIVY_CROSS_SYSROOT=${STAGING_DIR}

#ifeq ($(BR2_PACKAGE_HAS_LIBEGL),y)
#PYTHON_KIVY_DEPENDENCIES += libegl
#PYTHON_KIVY_ENV += USE_EGL=1
#endif

PYTHON_KIVY_DEPENDENCIES += sdl2 sdl2_image sdl2_mixer sdl2_ttf
PYTHON_KIVY_ENV += USE_SDL2=1
PYTHON_KIVY_ENV += KIVY_SDL2_PATH=$(STAGING_DIR)/usr/include/SDL2

define PYTHON_KIVY_REMOVE_EXAMPLES
	rm -rf $(TARGET_DIR)/usr/share/kivy-examples
endef

PYTHON_KIVY_POST_INSTALL_TARGET_HOOKS += PYTHON_KIVY_REMOVE_EXAMPLES

$(eval $(python-package))
