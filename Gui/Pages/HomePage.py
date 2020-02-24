from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from Gui.Pages.BasePage import BaseScreen
from Gui.GuiPagesConsts import PageNames


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.clearcolor = (1.0, 1.0, 1.0, 1.0)
        self.add_widget(BaseScreen())
        inner_grid = GridLayout(padding=[10, 10, 10, 10])
        btn = Button(text="My Button")
        inner_grid.add_widget(btn)
        self.add_widget(inner_grid)
        # self.layout = GridLayout()
        # self.layout.cols = 1
        # btn = Button(text="Go next")
        # btn.bind(on_press=self.go_to_second_page)
        # self.layout.add_widget(btn)
        # self.add_widget(self.layout)

    # def build_inner_grid(self):
    #     pass

    # def go_to_second_page(self, instance):
    #     self.manager.current = PageNames.BACKGROUND.name
