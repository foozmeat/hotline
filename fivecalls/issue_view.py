from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.controls import FCContactButton, FCListLabel, FCTextLabel
from fivecalls.toolbar import FCToolbar
from fivecalls.data import Issue


def button_callback(instance: FCContactButton):
    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'

    iv = IssueView(issue=instance.issue)

    root.add_widget(iv)
    root.current = root.next()


class IssueView(Screen):

    def __init__(self, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.kc = KivyConfig()

        self.layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                spacing=10,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.layout.add_widget(FCToolbar())

        name_label = FCListLabel(text=issue.name)

        self.layout.add_widget(name_label)

        reason_label = FCTextLabel(text=issue.reason)
        self.layout.add_widget(reason_label)

        call_label = FCListLabel(text="Call your representatives")

        self.layout.add_widget(call_label)

        for c in self.issue.contacts:
            c_button = FCContactButton(contact=c)
            self.layout.add_widget(c_button)

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)
