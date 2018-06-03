from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.controls import FCListLabel, FCTextLabel, FCContactLayout
from fivecalls.data import Issue


class IssueView(Screen):

    def __init__(self, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.kc = KivyConfig()

        self.layout = BoxLayout(
                orientation='vertical',
                # padding=(10, 10),
                size_hint_y=None,
                spacing=10,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        name_label = FCListLabel(
                text=issue.name,
                bold=True,
                padding=('20sp', '30sp')
        )

        self.layout.add_widget(name_label)

        reason_label = FCTextLabel(text=issue.reason)
        self.layout.add_widget(reason_label)

        call_label = FCListLabel(
                text="Call your representatives",
                bold=True,
                padding=('20sp', '30sp'),
                halign="center"
        )
        self.layout.add_widget(call_label)

        for c in self.issue.contacts:
            c_button = FCContactLayout(contact=c)
            self.layout.add_widget(c_button)

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)

    def on_pre_enter(self, *args):
        super().on_enter(*args)

        for c in self.layout.children:
            c.font_size = self.kc.font_size
            c.text_size = (self.kc.width, None)
