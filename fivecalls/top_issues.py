import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from fivecalls.config import KivyConfig


class TopIssueList(App):

    def build(self):
        kc = KivyConfig()

        layout = BoxLayout(orientation='vertical')

        top_label = Label(text='Top Issues')
        top_label.font_size = 20.0 * kc.scale

        layout.add_widget(top_label)

        with open('/tmp/fivecalls.json', 'r') as fp:
            data = json.load(fp)

        for i in data['issues']:
            if not i['inactive']:
                btn = Button(text=i['name'])
                btn.font_size = 20.0 * kc.scale
                btn.text_size = (kc.width, None)
                btn.halign = 'center'
                layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    TopIssueList().run()
