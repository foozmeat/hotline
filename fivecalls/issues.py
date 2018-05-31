from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from fivecalls.config import KivyConfig
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
                # row_default_height='48dp',
                # row_force_default=True,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        top_label = Label(
                text='[b]Top Issues[/b]',
                markup=True,
                font_size=self.kc.font_size,
                size_hint_y=None,
        )

        self.layout.add_widget(top_label)

        item_count = 1

        for i in fcd.issues:
            if not i.inactive:
                btn = Button(
                        text=i.name,
                        font_size=self.kc.font_size,
                        text_size=(self.kc.width, None),
                        halign='center',
                        size_hint_y=None,
                )
                self.layout.add_widget(btn)
                item_count += 1

        more = Label(
                text="[b]More Issues[/b]",
                markup=True,
                font_size=self.kc.font_size,
                text_size=(self.kc.width, None),
                halign='center',
                size_hint_y=None
        )
        self.layout.add_widget(more)
        item_count += 1

        for cat in fcd.categories:
            cat_label = Label(
                    text=f"[b]{cat}[/b]",
                    markup=True,
                    font_size=self.kc.font_size,
                    text_size=(self.kc.width, None),
                    halign='center',
                    size_hint_y=None
            )
            self.layout.add_widget(cat_label)
            item_count += 1

        self.scrollview = ScrollView(
                do_scroll_x=False
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)

    def on_pre_enter(self, *args):

        super().on_enter(*args)

        for c in self.layout.children:
            c.font_size = self.kc.font_size
