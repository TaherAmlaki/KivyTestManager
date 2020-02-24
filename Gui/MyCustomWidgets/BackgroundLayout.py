from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from Gui.MyCustomWidgets.MyCustomTransitions import MyWipeTransition


class StaticBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.bg = Rectangle(source='../assets/rabobank.png', pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg)
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class MyStaticScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StaticBackground())


class TestApp(App):
    def build(self):
        Config.set('kivy', 'window_icon', '../assets/rabobank-icon.png')
        sm = ScreenManager(transition=MyWipeTransition())
        sm.add_widget(MyStaticScreen(name='background'))
        sm.current = "background"
        return sm


if __name__ == '__main__':
    app = TestApp()
    try:
        app.run()
    except Exception as ex:
        raise ex
