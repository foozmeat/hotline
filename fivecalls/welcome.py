from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from fivecalls.config import KivyConfig
from fivecalls.controls import FCListButton, FCListLabel, FCBaseLabel, add_debug_rect, FCTextLabel
from fivecalls.helpers import random_color
from fivecalls.toolbar import FCToolbar
from fivecalls.issues import ISSUES_SCREEN

WELCOME_SCREEN = 'Welcome Screen'


def button_callback(instance: FCListButton):
    # kc = KivyConfig()
    # kc.set_font_size_in_pixels(instance.font_size)

    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'
    root.current = ISSUES_SCREEN


class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kc = KivyConfig()

        layout = StackLayout(
                # orientation='vertical',
        )

        self.add_widget(layout)

        layout.add_widget(FCToolbar(back_hidden=True))

        welcome_text_label = FCTextLabel(
            text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.")
        layout.add_widget(welcome_text_label)

        # layout.add_widget(Widget())  # This will fill up any empty space

        start = FCListButton(text="Start")
        start.bind(on_press=button_callback)
        layout.add_widget(start)
