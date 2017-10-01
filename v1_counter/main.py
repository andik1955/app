from kivy.app import App
from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class StartScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        self.counterVar = 1
        self.counterString = str(self.counterVar)

        self.counter = Label(text=self.counterString)
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
        if self.counterVar > 1:
            self.counterVar -= 1
            self.counter.text = str(self.counterVar)
'''
        else:
            self.grid = GridLayout(rows = 2)
            self.label = Label(text="You don't get stronger without training!")
            self.close = Button(text='I know ...').bind(on_click=p_up.dismiss)

            self.grid.add_widget(self.label)
            self.grid.add_widget(self.close)

            self.p_up = Popup(content = self.grid)
            #self.p_up.content.grid.close.bind(on_click = self.p_up.dismiss())
            self.p_up.open()
'''


class MainApp(App):
    def build(self):
        return StartScreen()

if __name__ == '__main__':
    MainApp().run()
