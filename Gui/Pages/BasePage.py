from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from Gui.GuiPagesConsts import PageNames
from MyUtils import MyPath


class StaticBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.bg = Rectangle(source=MyPath.Paths.RABO_ICON.value, pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg)
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        grid = BoxLayout(orientation='horizontal', padding=[10, 10, 10, 20])
        grid.add_widget(GridLayout())
        right_layout = GridLayout(padding=[10, 10, 10, 10], cols=1, spacing=2)
        right_layout.add_widget(GridLayout())
        right_layout.add_widget(StaticBackground(pos_hint = {'x': 0, 'center_y': .5}))
        grid.add_widget(right_layout)
        self.add_widget(grid)

    def on_enter(self):
        Clock.schedule_once(self.set_background_removal, 1)

    def set_background_removal(self, dt):
        self.manager.current = PageNames.HOME_PAGE.name
