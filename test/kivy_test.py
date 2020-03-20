from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import StringProperty
from kivy.properties import ListProperty

from kivy.event import EventDispatcher
from kivy.lang import Builder

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from widget.myboxlayout import MyBoxLayout

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyClass(EventDispatcher):
    dynamic_text = StringProperty('Start')


class MyPaintApp(App):
    def build(self):
        prop_class = MyClass()

        parent = MyBoxLayout()
        self.painter = MyPaintWidget()
        clearbtn = Button(text=prop_class.dynamic_text)
        #clearbtn.bind(on_release=parent.update_color)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)

        def update(instance, value):
            clearbtn.text = 'ok'
            #value
            pass
        # prop_class.bind(dynamic_text=clearbtn.setter('text'))
        prop_class.bind(dynamic_text=update)
        prop_class.dynamic_text = "ciapo"

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
