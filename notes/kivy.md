Installing on Raspbian

```
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev libmtdev1

Install Python 3.6 from source

/opt/python3.6/bin/pip3.6 install -U Cython==0.28.2
pip3 install pipenv

pip3 install git+https://github.com/kivy/kivy.git@master
```
