from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import sp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

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


def update_font_size(obj, value):
    obj.font_size = sp(value)


#
# Labels
#

class FCBaseLabel(Label):
    kc = ObjectProperty(KivyConfig())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(texture=my_height_callback)
        self.kc.bind(font_size=update_font_size)


class FCListLabel(FCBaseLabel):
    """ For list headers """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FCTextLabel(FCBaseLabel):
    """ For blocks of text """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FCHeaderLabel(FCBaseLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FCSectionLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_text(self, instance, value):
        self.text = value.upper()


class FCSectionLabelWithBorder(FCSectionLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FCCategoryLabel(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#
# Buttons
#

class FCListButton(Button):
    kc = ObjectProperty(KivyConfig())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(texture=my_height_callback)
        self.kc.bind(font_size=update_font_size)


class RoundedListButton(FCListButton):
    up_color = ListProperty([1, 0, 0, 1])
    down_color = ListProperty([0, 1, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FCIssueButton(Button):
    category = StringProperty()
    name = StringProperty()

    def __init__(self, issue=None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.category = self.issue.categories[0]['name'].upper()
        self.name = self.issue.name

    def on_issue(self, instance, issue):
        self.ids.category_label.text = issue.categories[0]['name']
        self.ids.name_label.text = issue.name


class FCContactButton(Button):
    person_name = StringProperty()
    person_area = StringProperty()
    person_image = StringProperty()
    person_reason = StringProperty()
    kc = ObjectProperty(KivyConfig())

    def __init__(self, contact: dict = None, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.contact = contact

        self.person_name = contact['name']
        self.person_image = IMAGE_PATH + contact['id'] + '.jpg'
        self.person_area = contact['area']
        self.person_reason = contact['reason']


class FCContactButtonWithBorder(FCContactButton):
    pass


class FCContactCard(Widget):
    person_name = StringProperty()
    person_area = StringProperty()
    person_image = StringProperty()
    person_reason = StringProperty()
    kc = ObjectProperty(KivyConfig())

    def __init__(self, contact: dict = None, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.contact = contact

        self.person_name = contact['name']
        self.person_image = IMAGE_PATH + contact['id'] + '.jpg'
        self.person_area = contact['area']
        self.person_reason = contact['reason']
