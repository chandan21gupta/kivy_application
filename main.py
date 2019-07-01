#required modules
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#required version
kivy.require("1.11.1")

#First page UI
class Page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		#Widgets

		#Widget - IP
		self.add_widget(Label(text="IP:"))
		self.ip = TextInput(multiline = False)
		self.add_widget(self.ip)

		#Widget - Port
		self.add_widget(Label(text="Port:"))
		self.port = TextInput(multiline = False)
		self.add_widget(self.port)

		#Widget - Username
		self.add_widget(Label(text="Username:"))
		self.username = TextInput(multiline = False)
		self.add_widget(self.username)

#Building the app
class MyApp(App):
	def build(self):
		return Page()

#Running the app
if __name__ == "__main__":
	MyApp().run()