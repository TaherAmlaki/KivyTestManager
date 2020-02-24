# https://kivy.org/doc/stable/installation/installation-windows.html
# python -m pip install --upgrade pip wheel setuptools virtualenv
# python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
# python -m pip install kivy_deps.angle==0.1.*
# python -m pip install kivy==1.11.1
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, WipeTransition, SlideTransition
from Gui.MyCustomWidgets.MyCustomTransitions import MyWipeTransition
from Gui.Pages.BasePage import BaseScreen
from Gui.Pages.HomePage import HomeScreen
from Gui.GuiPagesConsts import PageNames


class TestApp(App):
    title = "My Test App"

    def build(self):
        self.icon = './assets/rabobank-icon.png'
        Window.bind(on_request_close=self.on_request_close)
        sm = ScreenManager(transition=MyWipeTransition())
        sm.add_widget(BaseScreen(name=PageNames.BACKGROUND.name))
        sm.add_widget(HomeScreen(name=PageNames.HOME_PAGE.name))
        sm.current = PageNames.BACKGROUND.name
        return sm

    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Do you want to close the app?')
        return True

    def textpopup(self, title='', text=''):
        box = GridLayout(cols=1, size_hint_x=0.25)
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(0.5, 0.5))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(0.3, 0.4))
        mybutton.bind(on_release=self.stop)
        popup.open()


if __name__ == '__main__':
    app = TestApp()
    try:
        app.run()
    except Exception as ex:
        raise ex