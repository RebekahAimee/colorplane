from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.storage.jsonstore import JsonStore

import json

# APP CLASS
class ColorplaneApp(App):
    pass

# MAIN SCREEN
class Body():
    def __init__(self, **kwargs):
        # later
        pass

    def on_touch_down(self, touch):
        # put marks down
        pass

# MAIN MENU
class MainMenu(BoxLayout):
    pass

# SUBMENUS
class ColorMenu(BoxLayout):
    pass

class PaletteMenu(BoxLayout):
    pass

class DonateMenu(BoxLayout):
    pass

if __name__ == '__main__':
    ColorplaneApp().run()

