from kivy import Config
Config.set('graphics', 'width', 480)
Config.set('graphics', 'height', 800)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from fivecalls.views.issues import IssueList, ISSUES_SCREEN
from fivecalls.views.welcome import WelcomeScreen, WELCOME_SCREEN

Builder.load_file('fivecalls/templates/controls.kv')
Builder.load_file('fivecalls/templates/contact_button.kv')
Builder.load_file('fivecalls/templates/toolbar.kv')
Builder.load_file('fivecalls/templates/welcome.kv')
Builder.load_file('fivecalls/templates/issue_button.kv')
Builder.load_file('fivecalls/templates/call_button.kv')


class FiveCallsApp(App):
    title = "Five Calls"

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        fc_screen = ScreenManager()
        fc_screen.add_widget(WelcomeScreen(name=WELCOME_SCREEN))
        fc_screen.add_widget(IssueList(name=ISSUES_SCREEN))

        return fc_screen


if __name__ == '__main__':

    FiveCallsApp().run()
