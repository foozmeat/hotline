import os
import platform

from kivy.config import Config
from kivy.event import EventDispatcher
from kivy.metrics import sp
from kivy.properties import NumericProperty

from fivecalls.singleton import Singleton


class KivyConfig(EventDispatcher, metaclass=Singleton):
    font_size = NumericProperty(20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if platform.system() != 'Darwin':
            Config.set('input', 'pitft', 'mtdev,/dev/input/event0,rotation=270,invert_y=1')

        self.width = sp(480)
        self.height = sp(800)
        self.debug = os.getenv('DEBUG', False)

    def font_size_callback(self, obj, value):
        print(obj)
        obj.font_size = self.font_size


if __name__ == '__main__':
    kc = KivyConfig()
    kc2 = KivyConfig()
    assert (id(kc) == id(kc2))

