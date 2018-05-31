import platform
import subprocess

from kivy.config import Config
from kivy.metrics import MetricsBase

from fivecalls.singleton import Singleton


class KivyConfig(metaclass=Singleton):

    def __init__(self):
        mb = MetricsBase()
        self.scale = mb.density

        if platform.system() != 'Darwin':
            Config.set('input', 'pitft', 'mtdev,/dev/input/event2,rotation=270')

        self.padding = 20
        self.width = (480 * self.scale)
        self.height = (800 * self.scale)
        self.font_size = (20, 'sp')

        print(f"display scale: {self.scale}")

    def set_font_size_in_pixels(self, size):

        sp = size / self.scale

        self.font_size = (sp, 'sp')
        print(f"Font size changed to {self.font_size}")


if __name__ == '__main__':
    kc = KivyConfig()
    kc2 = KivyConfig()
    assert (id(kc) == id(kc2))
