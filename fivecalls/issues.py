from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

from fivecalls.config import KivyConfig
from fivecalls.controls import FCIssueButton, FCListLabel
from fivecalls.toolbar import FCToolbar
from fivecalls.data import FiveCallsData
from fivecalls.issue_view import IssueView

ISSUES_SCREEN = 'Issues'



def button_callback(instance: FCIssueButton):

    root = instance.get_root_window().children[0]  # type: ScreenManager
    root.transition.direction = 'left'

    # Build an IssueView on the fly and add it to the screen manager.
    iv = IssueView(issue=instance.issue)
    iv.name = f"dynamic_issue_view"

    root.add_widget(iv)
    root.current = root.next()


class IssueList(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kc = KivyConfig()
        fcd = FiveCallsData()

        self.layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.layout.add_widget(FCToolbar())

        top_label = FCListLabel(text='Top Issues', bold=True)
        self.layout.add_widget(top_label)

        for i in fcd.active_issues:
            btn = FCIssueButton(text=i.name, issue=i)
            btn.bind(on_press=button_callback)

            self.layout.add_widget(btn)

        for cat in fcd.categories:
            cat_label = FCListLabel(text=cat, bold=True)
            self.layout.add_widget(cat_label)

            issues = fcd.categories[cat]

            for i in issues:
                if i.inactive:
                    btn = FCIssueButton(text=i.name, issue=i)
                    btn.bind(on_press=button_callback)

                    self.layout.add_widget(btn)

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)

    # def on_pre_enter(self, *args):
    #
    #     super().on_enter(*args)
    #
    #     for c in self.layout.children:
    #         c.font_size = self.kc.font_size
    #         c.text_size = (self.kc.width, None)
