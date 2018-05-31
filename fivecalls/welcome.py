from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from fivecalls.config import KivyConfig


class SizeButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kc = KivyConfig()

        layout = BoxLayout(orientation='vertical')

        welcome_text_label = Label(text='Welcome', font_size=kc.font_size)
        layout.add_widget(welcome_text_label)

        font_select_label = Label(text='Please select a comfortable text size', font_size=kc.font_size)
        font_select_label.size_hint_y = None
        layout.add_widget(font_select_label)

        def button_callback(instance):
            print(f'The button {instance.font_size} is being pressed')
            Config.set('kivy', 'font_size', instance.font_size)

        for font_size in [12, 18, 22, 24]:
            btn = Button(text="I can read this")
            btn.font_size = (font_size, "sp")
            btn.size_hint_y = None
            btn.bind(on_press=button_callback)
            layout.add_widget(btn)

        self.add_widget(layout)
