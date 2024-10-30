from docutils.nodes import label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label



class Seesight(App):
    def build(self):
        self.icon = "Seesight.png"
        Label.text = "Welcome to Seesight".upper()
        self.message = """
            You are being part of the community now
        """
        return Label()



#running the app
if __name__ == "__main__":
    app = Seesight() #creating variable to run the app or just do Seesight().run()
    #running upp
    app.run()