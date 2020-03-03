# https://kivy.org/doc/stable/installation/installation-windows.html
# python -m pip install --upgrade pip wheel setuptools virtualenv
# python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
# python -m pip install kivy_deps.angle==0.1.*
# python -m pip install kivy==1.11.1
from MyUtils import MyPath
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from Gui.Pages.BasePage import BaseScreen
from Gui.Pages.HomePage import HomeScreen
from Gui.Pages.ConfigurationPage import ConfigurationScreen
from Gui.GuiPagesConsts import PageNames


class TestApp(App):
    title = "My Test App"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(BaseScreen(name=PageNames.BACKGROUND.name))
        self.sm.add_widget(HomeScreen(name=PageNames.HOME_PAGE.name))
        self.sm.add_widget(ConfigurationScreen(name=PageNames.CONFIGURATION.name))
        self._popup_exit = None
        # Window.bind(on_keyboard=self.on_key)

    def build(self):
        self.icon = MyPath.Paths.RABO_ICON.value
        Window.clearcolor = (0.25, 0.25, 0.25, 1)
        Window.bind(on_keyboard=self.on_key)
        Window.bind(on_request_close=self.on_request_close)
        self.sm.current = PageNames.BACKGROUND.name
        return self.sm

    def on_key(self, window, key, *args):
        if key in [276] and self.sm.current != PageNames.HOME_PAGE.name:
            self.sm.transition.direction = 'right'
            self.sm.current = self.sm.previous()

    def on_request_close(self, *args, **kwargs):
        if kwargs.get("source") != 'keyboard':
            self.textpopup(title='Exit', text='Do you want to close the app?')
        return True

    def textpopup(self, title='', text=''):
        box = GridLayout(cols=1, size_hint_x=0.25)
        box.add_widget(Label(text=text))

        button_grid = GridLayout(cols=2, size_hint_x=0.5, size_hint_y=0.35)
        ok_button = Button(text='YES', size_hint=(0.25, 0.3))
        ok_button.bind(on_release=self.stop)
        button_grid.add_widget(ok_button)
        cancel_button = Button(text="NO", size_hint=(0.25, 0.3))
        cancel_button.bind(on_release=lambda *args: self._popup_exit.dismiss())
        button_grid.add_widget(cancel_button)

        box.add_widget(button_grid)
        self._popup_exit = Popup(title=title, content=box, size_hint=(0.3, 0.4))
        self._popup_exit.open()
