from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.label import Label


def my_height_callback(obj, texture: Texture):

    if texture:
        obj.height = max(texture.size[1], 100)


class FCListButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.markup = True
        self.size_hint = (1, None)
        self.halign = 'center'
        self.padding = ('20sp', '20sp')

        self.bind(texture=my_height_callback)


class FCListLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.markup = True
        self.size_hint_y = None
        self.halign = 'center'
        self.padding = ('20sp', '20sp')

        self.bind(texture=my_height_callback)
