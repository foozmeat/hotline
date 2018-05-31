from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.controls import FCListButton, FCListLabel
from fivecalls.data import FiveCallsData

ISSUES_SCREEN = 'Top Issues'


class IssueList(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()
        fcd = FiveCallsData()

        self.layout = BoxLayout(
                orientation='vertical',
                padding=(10, 10),
                size_hint_y=None,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        top_label = FCListLabel(text='[b]Top Issues[/b]')

        self.layout.add_widget(top_label)

        for i in fcd.issues:
            if not i.inactive:
                btn = FCListButton(text=i.name)
                self.layout.add_widget(btn)

        for cat in fcd.categories:
            cat_label = FCListLabel(text=f"[b]{cat}[/b]")
            self.layout.add_widget(cat_label)

            issues = fcd.categories[cat]

            for i in issues:
                if i.inactive:
                    btn = FCListButton(text=i.name)
                    self.layout.add_widget(btn)

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
