from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.views.toolbar import FCToolbar
from fivecalls.data import Issue


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

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)
