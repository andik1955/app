from kivy.app import App
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class StartScreen(GridLayout):



    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        self.counterVar = NumericProperty(1)

        self.counter = Label(text=self.counterVar)
        self.minusButton = Button(text="-")
        self.plusButton = Button(text="+")



        self.plusButton.bind(on_press=self.updatePlus)
        self.minusButton.bind(on_press=self.updateMinus)

        self.cols = 3
        self.add_widget(self.minusButton)
        self.add_widget(self.counter)
        self.add_widget(self.plusButton)

    def updatePlus(self, event):
        self.counterVar += 1
        self.counter.text = str(self.counterVar)

    def updateMinus(self, event):
        self.counterVar -= 1
        self.counter.text = str(self.counterVar)

class MainApp(App):
    def build(self):
        return StartScreen()

if __name__ == '__main__':
    MainApp().run()
