from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

'''
class NumProp(Screen):

    counter = 1
    def countUp(self):
        self += 1
        return str(self)
    def countDown(self):
        self = self - 1
        return str(self)
    pass
'''
class StartScreen(Screen):
    pass

class SetWorkout(Screen):
    pass

class SetSession(Screen):
    pass

class SetTake(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()
