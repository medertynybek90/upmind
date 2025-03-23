from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Загружаем разметку из KV-файла
class MainScreen(Screen):
    pass

class HabitTrackerApp(App):
    def build(self):
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    HabitTrackerApp().run()
