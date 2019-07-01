#required modules
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


#required version
kivy.require("1.11.1")

class Page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		#Widgets
		self.add_widget(Label(text="IP:"))
		self.ip = TextInput(multiline = False)
		self.add_widget(self.ip)

		self.add_widget(Label(text="Port:"))
		self.port = TextInput(multiline = False)
		self.add_widget(self.port)

		self.add_widget(Label(text="Username:"))
		self.username = TextInput(multiline = False)
		self.add_widget(self.username)





class MyApp(App):
	def build(self):
		return Page()







if __name__ == "__main__":
	MyApp().run()