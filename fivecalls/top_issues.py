import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from fivecalls.config import KivyConfig
from fivecalls.data import JSON_PATH, FiveCallsData


class TopIssueList(App):

    def build(self):
        kc = KivyConfig()
        fcd = FiveCallsData()

        layout = BoxLayout(orientation='vertical')

        top_label = Label(text='Top Issues')
        top_label.font_size = kc.font_size

        layout.add_widget(top_label)

        for i in fcd.issues:
            if not i.inactive:
                btn = Button(text=i.name)
                btn.font_size = kc.font_size
                btn.text_size = (kc.width, None)
                btn.halign = 'center'
                # btn.size_hint_y = None
                layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    TopIssueList().run()
