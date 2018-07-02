from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.data import Issue
from fivecalls.views.call_view import CallView
from fivecalls.views.controls import FCCategoryLabel, FCContactButton, FCHeaderLabel, FCSectionLabel, FCTextLabel, \
    FCSectionLabelWithBorder, FCContactButtonWithBorder
from fivecalls.views.toolbar import FCToolbar


def button_callback(instance: FCContactButton):
    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'

    cv = CallView(issue=instance.issue, contact=instance.contact)
    cv.name = f"dynamic_call_view"

    root.add_widget(cv)
    root.current = root.next()


class IssueView(Screen):

    def __init__(self, issue: Issue = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.kc = KivyConfig()

        self.layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.t = FCToolbar()
        self.t.back_label = '< Issues'
        self.layout.add_widget(self.t)

        hl = FCHeaderLabel(text=issue.name)
        hl.font_size = sp(30)
        self.layout.add_widget(hl)

        c_label = FCCategoryLabel()
        c_label.text = self.issue.categories[0]['name'].upper()
        self.layout.add_widget(c_label)

        # newline added to push 'calls' down a bit
        self.layout.add_widget(FCSectionLabelWithBorder(text="\nCalls"))

        for c in self.issue.contacts:
            c_button = FCContactButtonWithBorder(issue=self.issue, contact=c)
            c_button.bind(on_press=button_callback)
            self.layout.add_widget(c_button)

        self.layout.add_widget(FCSectionLabel(text="Background"))

        self.layout.add_widget(FCTextLabel(text=issue.reason))

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)

        # This is where a scroll hint would get hooked up
        # self.scrollview.bind(scroll_y=print)
