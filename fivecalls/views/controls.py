from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import sp
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

from fivecalls.config import KivyConfig
from fivecalls.data import IMAGE_PATH, Issue
from fivecalls.helpers import random_color


def add_debug_rect(obj):
    kc = KivyConfig()

    if kc.debug:
        with obj.canvas.before:
            random_color()
            Rectangle(pos=obj.pos, size=obj.size)


def my_height_callback(obj, texture: Texture):
    if texture:
        obj.height = max(texture.size[1], 50)


def my_size_callback(obj, texture: Texture):
    if texture:
        obj.size = texture.size

        kc = KivyConfig()

        if kc.debug:
            with obj.canvas.before:
                random_color()
                Rectangle(pos=obj.pos, size=obj.size)


#
# Labels
#

class FCBaseLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()
        self.font_size = sp(self.kc.font_size)
        self.text_size = (self.kc.width, None)
        self.size_hint_y = None
        self.bind(texture=my_height_callback)
        self.kc.bind(font_size=self.update_font_size)
        self.color = [0, 0, 0, 1]

    def update_font_size(self, obj, value):
        self.font_size = sp(value)


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


#
# Buttons
#

class FCListButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kc = KivyConfig()
        self.font_size = sp(self.kc.font_size)
        self.text_size = (self.kc.width, None)
        self.size_hint_y = None
        self.halign = 'center'
        self.padding = (sp(10), sp(10))

        self.bind(texture=my_height_callback)
        self.kc.bind(font_size=self.update_font_size)

    def update_font_size(self, obj, value):
        self.font_size = sp(value)


class FCIssueButton(FCListButton):

    def __init__(self, issue=None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue


class FCContactButton(Button):
    person_name = StringProperty()
    person_area = StringProperty()
    person_image = StringProperty()
    person_reason = StringProperty()

    def __init__(self, contact: dict = None, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()
        self.issue = issue
        self.contact = contact

        self.person_name = contact['name']
        self.person_image = IMAGE_PATH + contact['id'] + '.jpg'
        self.person_area = contact['area']
        self.person_reason = contact['reason']
