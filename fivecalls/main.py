from kivy import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from fivecalls.controls import FCContactLayout
from fivecalls.data import FiveCallsData
from fivecalls.issue_view import IssueView
from fivecalls.issues import IssueList, ISSUES_SCREEN
from fivecalls.welcome import WelcomeScreen, WELCOME_SCREEN


class FiveCallsApp(App):
    title = "Five Calls"

    def build(self):

        fcd = FiveCallsData()

        fc_screen = ScreenManager()
        # fc_screen.add_widget(WelcomeScreen(name=WELCOME_SCREEN))
        # fc_screen.add_widget(IssueList(name=ISSUES_SCREEN))

        fc_screen.add_widget(IssueView(issue=fcd.issues[0]))

        return fc_screen


if __name__ == '__main__':
    Config.set('graphics', 'width', 480)
    Config.set('graphics', 'height', 800)

    FiveCallsApp().run()
