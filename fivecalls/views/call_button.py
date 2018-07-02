from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.metrics import sp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

from fivecalls.config import KivyConfig

BLUE = (0, 118 / 255, 1, 1)
RED = (208 / 255, 2 / 255, 27 / 255, 1)


class CallButton(Button):
    kc = ObjectProperty(KivyConfig())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rect = None

        self.bind(pos=self.update_rect,
                  size=self.update_rect)
        self.set_call()

    def set_background(self, color):
        # self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)
            self.rect = RoundedRectangle(
                    radius=[20]
            )

    def set_call(self):
        self.set_background(BLUE)
        self.text = "Call"
        self.disabled = False

    def set_ringing(self):
        self.set_background(RED)
        self.text = "Ringing…"
        self.disabled = True

    def set_hang_up(self):
        self.set_background(RED)
        self.text = "Hang Up"
        self.disabled = False

    def update_rect(self, *args):
        self.rect.pos = (self.pos[0] + sp(40), self.pos[1])
        self.rect.size = (self.size[0] - sp(80), self.size[1])
