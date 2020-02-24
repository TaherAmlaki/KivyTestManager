from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from Gui.Pages.BasePage import BaseScreen
from Gui.GuiPagesConsts import PageNames, ButtonColor


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BaseScreen())
        self.inner_grid = GridLayout(padding=[10, 10, 10, 10], cols=2)
        self.add_widget(self.build_inner_grid())

    def build_inner_grid(self):
        main_layout = GridLayout(padding=[10, 10, 10, 10], cols=2)
        left_layout = GridLayout(padding=[10, 10, 10, 10], cols=1, size_hint_x=0.5)
        btn = Button(text="Configuration", background_color=ButtonColor.NORMAL.value)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text="Overview", background_color=ButtonColor.NORMAL.value)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text="Review", background_color=ButtonColor.NORMAL.value)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        main_layout.add_widget(left_layout)
        main_layout.add_widget(GridLayout(cols=1))
        return main_layout

    def _on_button_pressed(self, instance):
        pass

    # def go_to_second_page(self, instance):
    #     self.manager.current = PageNames.BACKGROUND.name
