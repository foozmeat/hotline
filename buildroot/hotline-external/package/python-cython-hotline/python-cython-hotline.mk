################################################################################
#
# cython
#
################################################################################

PYTHON_CYTHON_HOTLINE_VERSION = 0.28.2
PYTHON_CYTHON_HOTLINE_SOURCE = Cython-$(PYTHON_CYTHON_HOTLINE_VERSION).tar.gz
PYTHON_CYTHON_HOTLINE_SITE = https://files.pythonhosted.org/packages/79/9d/dea8c5181cdb77d32e20a44dd5346b0e4bac23c4858f2f66ad64bbcf4de8
PYTHON_CYTHON_HOTLINE_SETUP_TYPE = setuptools
PYTHON_CYTHON_HOTLINE_LICENSE = Apache-2.0
PYTHON_CYTHON_HOTLINE_LICENSE_FILES = COPYING.txt LICENSE.txt

$(eval $(host-python-package))
