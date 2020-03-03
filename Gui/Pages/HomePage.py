from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from Gui.Pages.BasePage import BaseScreen
from Gui.GuiPagesConsts import PageNames, ButtonColor


class HomeScreen(Screen):

    CONFIGURATION = "Configuration"
    TEST_RESULTS_OVERVIEW = "Overview Test Results"
    EXECUTIONS_REVIEW = "Review of Executions"
    ADD_A_TEST = "Add A New Test"
    CREATE_NEW_BATCH = "Create A New Batch"
    RUN_A_BATCH = "Run A Test Batch"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BaseScreen())
        self.inner_grid = GridLayout(padding=[10, 10, 10, 10], cols=2)
        self.add_widget(self.build_inner_grid())

    def build_inner_grid(self):
        btn_color = ButtonColor.NORMAL.value
        main_layout = GridLayout(padding=[10, 10, 10, 10], cols=2)
        left_layout = GridLayout(padding=[10, 10, 10, 10], cols=1, size_hint_x=0.75, spacing=2)
        btn = Button(text=HomeScreen.CONFIGURATION, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text=HomeScreen.TEST_RESULTS_OVERVIEW, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text=HomeScreen.EXECUTIONS_REVIEW, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text=HomeScreen.ADD_A_TEST, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text=HomeScreen.CREATE_NEW_BATCH, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        btn = Button(text=HomeScreen.RUN_A_BATCH, background_color=btn_color)
        btn.bind(on_press=self._on_button_pressed)
        left_layout.add_widget(btn)

        main_layout.add_widget(left_layout)
        main_layout.add_widget(GridLayout(cols=1))
        return main_layout

    def _on_button_pressed(self, instance):
        text = instance.text
        if text == HomeScreen.CONFIGURATION:
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = PageNames.CONFIGURATION.name
