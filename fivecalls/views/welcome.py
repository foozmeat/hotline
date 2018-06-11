from kivy.metrics import sp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from fivecalls.config import KivyConfig
from fivecalls.data import FiveCallsData
from fivecalls.views.controls import FCListButton, FCTextLabel
from fivecalls.views.toolbar import FCToolbar
from fivecalls.views.issues import ISSUES_SCREEN

WELCOME_SCREEN = 'Welcome Screen'


def button_callback(instance: FCListButton):
    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'
    root.current = ISSUES_SCREEN


class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fcd = FiveCallsData()

        layout = StackLayout(
                # orientation='vertical',
        )

        self.add_widget(layout)

        layout.add_widget(FCToolbar(back_hidden=True))

        welcome_text_label = FCTextLabel(
            text=f"MAKE YOUR VOICE HEARD\n\nCalling is the most effective way to influence your representatives.")
        layout.add_widget(welcome_text_label)

        stat_label = FCTextLabel(text=f"Together the 5 Calls community has contributed {fcd.global_count:,} calls!")
        layout.add_widget(stat_label)

        # layout.add_widget(Widget())  # This will fill up any empty space

        start = FCListButton(text="Start")
        start.bind(on_press=button_callback)
        layout.add_widget(start)
