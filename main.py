#required modules
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os
#required version
kivy.require("1.11.1")

#First page UI
class FirstPage(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		#If the file exists, login details will be incorporated, else new will be created
		if os.path.isfile("prev_details.txt"):
			with open("prev_details.txt","r") as f:
				d = f.read().split(",")
				prev_ip = d[0]
				prev_port = d[1]
				prev_username = d[2]
		else:
			prev_ip = ""
			prev_port = ""
			prev_username = ""
		#Widgets

		#Widget - IP
		self.add_widget(Label(text="IP:"))
		self.ip = TextInput(text=prev_ip,multiline = False)
		self.add_widget(self.ip)

		#Widget - Port
		self.add_widget(Label(text="Port:"))
		self.port = TextInput(text=prev_port,multiline = False)
		self.add_widget(self.port)

		#Widget - Username
		self.add_widget(Label(text="Username:"))
		self.username = TextInput(text=prev_username,multiline = False)
		self.add_widget(self.username)

		self.join = Button(text="Join")
		self.join.bind(on_press=self.join_button)
		self.add_widget(Label())
		self.add_widget(self.join)


	#Join Button
	def join_button(self, instance):
		port = self.port.text
		ip = self.ip.text
		username = self.username.text
		
		#print("Attempting to join "+ip+"-"+port+username)
		#saving the login details
		with open("prev_details.txt","w") as f:
			f.write(f"{ip},{port},{username}")

		info = f"Attempting to join {ip}:{port} as {username}"
		chat_app.info_page.update_info(info)

		chat_app.screen_manager.current = "Info"


class InfoPage(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.message = Label(halign="center",valign="middle",font_size=30)
		self.message.bind(width=self.update_text_width)
		self.add_widget(self.message)

	def update_info(self,message):
		self.message.text = message

	def update_text_width(self,*_):
		self.message.text_size = (self.message.width*0.9,None)




#Building the app
class MyApp(App):
	def build(self):
		#return FirstPage()
		self.screen_manager = ScreenManager()

		self.first_page = FirstPage()
		screen = Screen(name="Connect")
		screen.add_widget(self.first_page)
		self.screen_manager.add_widget(screen)

		self.info_page = InfoPage()
		screen = Screen(name="Info")
		screen.add_widget(self.info_page)
		self.screen_manager.add_widget(screen)

		return self.screen_manager
#Running the app
if __name__ == "__main__":
	chat_app = MyApp()
	chat_app.run()