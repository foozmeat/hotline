from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

from fivecalls.config import KivyConfig
from fivecalls.controls import FCListButton, FCListLabel
from fivecalls.issues import ISSUES_SCREEN

WELCOME_SCREEN = 'Welcome Screen'


def button_callback(instance: FCListButton):
    # kc = KivyConfig()
    # kc.set_font_size_in_pixels(instance.font_size)

    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.current = ISSUES_SCREEN


class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kc = KivyConfig()

        layout = BoxLayout(orientation='vertical')

        welcome_text_label = Label(text='Welcome', font_size=kc.font_size)
        layout.add_widget(welcome_text_label)

        start = FCListButton(text="Start")
        start.bind(on_press=button_callback)
        layout.add_widget(start)

        # font_select_label = FCListLabel(text='Please select a comfortable text size', font_size=kc.font_size)
        # font_select_label.size_hint_y = None
        # layout.add_widget(font_select_label)
        #
        # for font_size in range(12, 30, 3):
        #     btn = FCListButton(text="I can read this")
        #     btn.font_size = (font_size, "sp")
        #     btn.bind(on_press=button_callback)
        #
        #     layout.add_widget(btn)

        self.add_widget(layout)
