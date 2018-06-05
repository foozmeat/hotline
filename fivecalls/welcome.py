from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

from fivecalls.config import KivyConfig
from fivecalls.controls import FCListButton, FCListLabel, FCBaseLabel
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

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(FCToolbar(back_hidden=True))

        welcome_text_label = FCBaseLabel(text='Welcome', font_size=sp(kc.font_size))

        layout.add_widget(welcome_text_label)

        start = FCListButton(text="Start")
        start.bind(on_press=button_callback)
        layout.add_widget(start)

        self.add_widget(layout)
