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
        self.width = (480 * self.scale) - self.padding
        self.height = (800 * self.scale) - self.padding
        self.font_size = (20, 'sp')

        print(f"display scale: {self.scale}")


if __name__ == '__main__':
    kc = KivyConfig()

    kc2 = KivyConfig()

    assert (id(kc) == id(kc2))
