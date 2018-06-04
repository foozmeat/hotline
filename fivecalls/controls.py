from kivy.graphics.context_instructions import Color
from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

from fivecalls.config import KivyConfig
from fivecalls.data import IMAGE_PATH
from fivecalls.helpers import in_sps, random_color


def my_height_callback(obj, texture: Texture):
    if texture:
        obj.height = max(texture.size[1], 100)


def my_size_callback(obj, texture: Texture):
    kc = KivyConfig()

    if texture:
        obj.size = texture.size

    if kc.debug:
        with obj.canvas:
            random_color()
            Rectangle(pos=obj.pos, size=obj.size)


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

        ROW_HEIGHT = 100
        X_PAD = 10
        Y_PAD = 10

        self.kc = KivyConfig()
        self.contact = contact
        # self.text_size = (self.kc.width, None)

        self.size_hint = (None, None)
        self.size = (self.kc.width, in_sps(ROW_HEIGHT))

        if self.kc.debug:
            with self.canvas:
                random_color()
                Rectangle(size=self.size)

        # Contact Image
        c_img = Image(source=IMAGE_PATH + contact['id'])
        c_img.size_hint = (None, None)
        c_img.height = in_sps(ROW_HEIGHT - (Y_PAD * 2))
        c_img.y = in_sps(Y_PAD)
        self.add_widget(c_img)

        # Contact Name

        name_label = Label(text=self.contact['name'], bold=True)
        name_label.bind(texture=my_size_callback)
        name_label.font_size = self.kc.font_size
        name_label.size_hint = (None, None)
        name_label.pos = (in_sps(100), in_sps(ROW_HEIGHT / 2))

        self.add_widget(name_label)

        # Area

        area_label = Label(text=self.contact['area'])
        area_label.bind(texture=my_size_callback)
        area_label.font_size = self.kc.font_size
        area_label.size_hint = (None, None)
        area_label.pos = (in_sps(100), 20)

        self.add_widget(area_label)
