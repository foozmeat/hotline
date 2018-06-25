from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager

from fivecalls.config import KivyConfig
from fivecalls.views.controls import FCListButton


class FCToolbarButton(FCListButton):
    pass


class FCSizePopup(Popup):

    kc = ObjectProperty(KivyConfig())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def size_change(self, value):
        self.kc.font_size = value


class FCToolbar(BoxLayout):

    back_hidden = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_hidden(self, instance, value):
        if value:
            button = self.ids.back_button  # type: Button
            button.opacity = 0
            button.disabled = True

    def back_callback(self):
        root = self.get_root_window().children[0]  # type: ScreenManager
        root.transition.direction = 'right'
        prev = root.previous()
        current = root.current

        root.current = prev

        if 'dynamic' in current:
            screen = root.get_screen(current)
            root.remove_widget(screen)

    def display_size_popover(self):
        popup = FCSizePopup()
        popup.open()
