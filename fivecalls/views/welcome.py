from kivy.uix.screenmanager import Screen, ScreenManager

from fivecalls.data import FiveCallsData
from fivecalls.views.controls import FCListButton
from fivecalls.views.issues import ISSUES_SCREEN

WELCOME_SCREEN = 'Welcome Screen'


def button_callback(instance: FCListButton):
    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'
    root.current = ISSUES_SCREEN


class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fcd = FiveCallsData()
        self.ids.start_button.bind(on_press=button_callback)
        self.ids.calls_label.text = f"Together the 5 Calls community has contributed {self.fcd.global_count:,} calls!"
