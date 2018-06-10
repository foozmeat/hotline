from kivy.core.window import Window
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.views.controls import FCTextLabel, FCListButton, FCContactButton
from fivecalls.views.toolbar import FCToolbar
from fivecalls.data import Issue


class CallButton(FCListButton):

    def __init__(self, number: str = None, **kwargs):
        super().__init__(**kwargs)

        self.number = number
        self.text = "Call"

    def on_press(self):
        super().on_press()


class OutcomeButton(FCListButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        super().on_press()


class CallView(Screen):

    def __init__(self, issue: Issue = None, contact: dict = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.contact = contact

        self.kc = KivyConfig()

        self.layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                spacing=10,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.layout.add_widget(FCToolbar())

        contact_button = FCContactButton(contact=self.contact)
        contact_button.disabled = True
        self.layout.add_widget(contact_button)

        call_button = CallButton()
        self.layout.add_widget(call_button)

        reason_label = FCTextLabel(text=issue.script)
        self.layout.add_widget(reason_label)

        button_layout = GridLayout(cols=2, size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))

        for model in issue.outcomeModels:
            b = OutcomeButton(
                    text=model['label'].title(),
            )
            button_layout.add_widget(b)
        self.layout.add_widget(button_layout)

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)
