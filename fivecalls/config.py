import platform
import subprocess

from kivy.config import Config


class KivyConfig:

    def __init__(self):
        self.scale = 1.0

        Config.set('kivy', 'exit_on_escape', 0)
        Config.set('kivy', 'desktop', 0)

        Config.set('graphics', 'width',  480)
        Config.set('graphics', 'height', 800)
        Config.set('graphics', 'borderless', 1)

        if platform.system() == 'Darwin':
            if 'Retina' in subprocess.getoutput('system_profiler SPDisplaysDataType'):
                self.scale = 2.0

        else:
            Config.set('input', 'pitft', 'mtdev,/dev/input/event2,rotation=270')

        self.padding = 20
        self.width = (480 * self.scale) - self.padding
        self.height = (800 * self.scale) - self.padding
