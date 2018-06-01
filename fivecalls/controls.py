from kivy.graphics.context_instructions import Color
from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

from fivecalls.config import KivyConfig


def my_height_callback(obj, texture: Texture):
    if texture:
        obj.height = max(texture.size[1], 100)


class FCListButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kc = KivyConfig()
        self.font_size = self.kc.font_size
        self.text_size = (self.kc.width, None)
        self.size_hint = (1, None)
        self.halign = 'center'
        self.padding = ('20sp', '20sp')

        self.bind(texture=my_height_callback)


class FCListLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.halign = 'center'
        self.padding = ('20sp', '20sp')

        self.bind(texture=my_height_callback)


class FCTextLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.padding = ('20sp', '20sp')

        self.bind(texture=my_height_callback)


class FCIssueButton(FCListButton):

    def __init__(self, issue=None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue


class FCContactLayout(RelativeLayout):

    def __init__(self, contact: dict = None, **kwargs):
        super().__init__(**kwargs)
        self.kc = KivyConfig()
        self.contact = contact
        # self.text_size = (self.kc.width, None)

        self.size_hint = (None, None)
        self.size = (self.kc.width, 200)

        with self.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(0, 0), size=self.size)

        name_label = Label(text=self.contact['name'])
        name_label.pos = (50, 0)
        # name_label.size = (self.kc.width, 100)
        # name_label.size_hint = (None, None)
        # name_label.halign = 'left'

        with name_label.canvas:
            Color(0, 1, 0, 0.5)
            Rectangle(pos=name_label.pos, size=name_label.size)

        self.add_widget(name_label)
