Installing on Raspbian

```
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev libmtdev1

pip3 install pipenv

pip3 install -U Cython==0.28.2
pip3 install git+https://github.com/kivy/kivy.git@master
```

Install on Mac OS X

```
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer python3 gst-plugins-base gst-plugins-good

pip3 install pipenv
export USE_OSX_FRAMEWORKS=0 
pipenv install

```
