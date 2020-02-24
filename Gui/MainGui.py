# https://kivy.org/doc/stable/installation/installation-windows.html
# python -m pip install --upgrade pip wheel setuptools virtualenv
# python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
# python -m pip install kivy_deps.angle==0.1.*
# python -m pip install kivy==1.11.1
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, WipeTransition, SlideTransition
from Gui.MyCustomWidgets.MyCustomTransitions import MyWipeTransition
from Gui.Pages.BasePage import BaseScreen
from Gui.Pages.HomePage import HomeScreen
from Gui.GuiPagesConsts import PageNames


class TestApp(App):
    title = "My Test App"

    def build(self):
        Config.set('kivy', 'window_icon', './assets/rabobank-icon.png')
        sm = ScreenManager(transition=MyWipeTransition())
        sm.add_widget(BaseScreen(name=PageNames.BACKGROUND.name))
        sm.add_widget(HomeScreen(name=PageNames.HOME_PAGE.name))
        sm.current = PageNames.BACKGROUND.name
        return sm


if __name__ == '__main__':
    app = TestApp()
    try:
        app.run()
    except Exception as ex:
        raise ex