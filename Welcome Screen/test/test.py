# Potential goals to bring about a solution to your problems

# Don't know how to do this with Kivy
# ^ Try to translate as much of this to Kivy as possible - see if I can get it to work.

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder

class SuperScrollView(ScrollView):
    """docstring for SuperScrollView."""



    def __init__(self, **kwargs):
        super(SuperScrollView, self).__init__(**kwargs)
        self.window_size = (Window.width, Window.height)


layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

# root = Builder.load_file("welcome.kv")

# scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
# root.add_widget(layout)

class testApp(App):

    def build(self):
        return root

if __name__ == '__main__':
	testApp().run()
