from kivy.clock import Clock
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from fivecalls.call_results import CallResults
from fivecalls.config import KivyConfig
from fivecalls.data import Issue
from fivecalls.sim8xx_manager import SIM8XXManager
from fivecalls.views.call_button import CallButton
from fivecalls.views.controls import FCContactCard, FCTextLabel, OutcomeButton
from fivecalls.views.toolbar import FCToolbar


class CallView(Screen):

    def __init__(self, issue: Issue = None, contact: dict = None, **kwargs):
        super().__init__(**kwargs)

        self.issue = issue
        self.contact = contact

        self.kc = KivyConfig()
        self.phone = SIM8XXManager()

        self.layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                spacing=10,
        )
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.layout.add_widget(FCToolbar())

        contact_button = FCContactCard(contact=self.contact)
        contact_button.disabled = True
        self.layout.add_widget(contact_button)

        self.call_button = CallButton()
        self.call_button.bind(on_press=self.call_button_pressed)
        self.layout.add_widget(self.call_button)

        reason_label = FCTextLabel(text=issue.script)
        self.layout.add_widget(reason_label)

        self.scrollview = ScrollView(
                do_scroll_x=False,
        )
        self.scrollview.add_widget(self.layout)
        self.add_widget(self.scrollview)

        self.outcome_popup = OutcomePopup(issue=issue, contact=contact)

    def call_button_pressed(self, obj: Widget):

        if self.phone.status == 0:
            self.phone.dial_number('5038163008')
            # self.phone.dial_number(self.contact['phone'])
            # obj.disabled = True

            Clock.schedule_interval(self.update_call_status, 0.5)
        else:
            self.phone.hang_up()
            self.outcome_popup.open()

    def update_call_status(self, dt):

        self.phone.get_phone_status()

        if self.phone.status == 0:
            # Call has ended
            self.call_button.set_call()
            self.outcome_popup.open()
            return False

        elif self.phone.status == 2:
            self.call_button.set_ringing()
            return True

        elif self.phone.status == 3:
            self.call_button.set_ringing()
            return True

        elif self.phone.status == 4:
            self.call_button.set_hang_up()
            return True


class OutcomePopup(Popup):
    def __init__(self, issue: Issue = None, contact=None, **kwargs):
        super().__init__(**kwargs)
        self.issue = issue
        self.contact = contact
        self.kc = KivyConfig()

        self.title = "What was the outcome of your call?"
        self.title_align = 'center'
        self.size_hint = 0.8, 0.25
        self.background = 'images/modalview-background.png'
        self.title_color = 0, 0, 0, 1
        self.separator_color = 1, 1, 1, 1
        self.title_size = sp(self.kc.font_size)
        self.auto_dismiss = False

        button_layout = GridLayout(cols=2, size_hint_y=None, spacing=[sp(10), sp(10)])
        button_layout.bind(minimum_height=button_layout.setter('height'))

        for model in issue.outcomeModels:
            b = OutcomeButton(
                    text=model['label'].title(),
            )
            b.bind(on_release=self.button_callback)
            button_layout.add_widget(b)

        self.content = button_layout

    def button_callback(self, button):
        cr = CallResults()
        cr.new_result(self.issue.id, self.contact['id'], self.contact['phone'], button.text.lower())
        self.dismiss()
