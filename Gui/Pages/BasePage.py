from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.gridlayout import GridLayout
from Gui.GuiPagesConsts import PageNames


class StaticBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.bg = Rectangle(source='./assets/rabobank-icon.png', pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg)
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.clearcolor = (1.0, .5, .0, .2)
        grid = GridLayout()
        grid.cols = 2
        grid.add_widget(GridLayout())
        right_layout = GridLayout()
        right_layout.cols = 1
        right_layout.add_widget(GridLayout())
        # right_layout.add_widget(StaticBackground(pos_hint=(300, 300)))
        right_layout.add_widget(StaticBackground())
        grid.add_widget(right_layout)
        self.add_widget(grid)

    def on_enter(self):
        print('enter')
        Clock.schedule_once(self.set_background_removal, 1)

    def set_background_removal(self, dt):
        self.manager.current = PageNames.HOME_PAGE.name
