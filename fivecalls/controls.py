from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import sp
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

from fivecalls.config import KivyConfig
from fivecalls.data import IMAGE_PATH
from fivecalls.helpers import random_color


def my_height_callback(obj, texture: Texture):
    if texture:
        obj.height = max(texture.size[1], 100)


def my_size_callback(obj, texture: Texture):
    if texture:
        obj.size = texture.size

        kc = KivyConfig()

        if kc.debug:
            with obj.canvas.before:
                random_color()
                Rectangle(pos=obj.pos, size=obj.size)


class FCBaseLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()
        self.font_size = self.kc.font_size
        self.text_size = (self.kc.width, None)
        self.size_hint_y = None
        self.bind(texture=my_height_callback)


class FCListLabel(FCBaseLabel):
    """ For list headers """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = (sp(20), sp(30))
        self.bold = True
        self.halign = 'center'


class FCTextLabel(FCBaseLabel):
    """ For blocks of text """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = (sp(20), sp(20))


class FCListButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kc = KivyConfig()
        self.font_size = self.kc.font_size
        self.text_size = (self.kc.width, None)
        self.size_hint_y = None
        self.halign = 'center'
        self.padding = (sp(20), sp(20))

        self.bind(texture=my_height_callback)


class FCIssueButton(FCListButton):

    def __init__(self, issue=None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue


class FCContactButton(Button):
    person_name = StringProperty()
    person_area = StringProperty()
    person_image = StringProperty()

    def __init__(self, contact: dict = None, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()

        self.person_name = contact['name']
        self.person_image = IMAGE_PATH + contact['id'] + '.jpg'
        print(self.person_image)
        self.person_area = contact['area']

