from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import Property, NumericProperty,\
    ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import *

#Function for changing the screen
def game_screen(*args):
	App.get_running_app().root.current = 'game'

class GomokuLogin(Screen):
	pass

class GomokuRooms(Screen):
	username = Property('')

	def setUsername(self, user):
		self.username = user

	def setRoomAmount(self, amount):
		self.roomAmount = amount

	def printRoom(self):
		roomAmount = 4
		self.ids.rooms.clear_widgets()
		if roomAmount > 0:
			for i in range (0,roomAmount):
				#Init
				roomName = Label(text="[color=F41D4E]Room 1[/color]", markup= True)
				tag1 = Label(text="Player :")
				mainGrid = GridLayout(cols= 2)

				#Setting Background - not function yet -
				#mainGrid.canvas.add(Color(1,1,1,.5))
				#mainGrid.canvas.add(Rectangle(pos=self.pos, size=self.size))

				#Process
					#adding roomname
				titleGrid = GridLayout(rows=2, padding=[5,10])
				titleGrid.add_widget(roomName)
					#adding button for room
				buttonGrid = GridLayout(rows=2, padding=[250,0])
				joinButton = Button(text='Join',on_press= game_screen)
				#joinButton.bind(on_press=change_screen('game'))
				watchButton = Button(text='Watch')
				buttonGrid.add_widget(joinButton)
				buttonGrid.add_widget(watchButton)

				titleGrid.add_widget(buttonGrid)
					#adding playername
				playerGrid = GridLayout(rows=4, padding=[5,10])
				playerGrid.add_widget(tag1)
				playerGrid.add_widget(Label(text='fauzan'))
				playerGrid.add_widget(Label(text='ahmad'))
				playerGrid.add_widget(Label(text='azwar'))
					#including roomname and playername
				mainGrid.add_widget(titleGrid)
				mainGrid.add_widget(playerGrid)

				#Render
				self.ids.rooms.add_widget(mainGrid)
		else:
			self.ids.rooms.add_widget(Label(text="No rooms available"))

class GomokuMakeRoom(Screen):
	pass

class GomokuGame(Screen):
	pass

class ScreenManager(ScreenManager):
	pass

presentation = Builder.load_file("gomoku.kv")

class GomokuApp(App):

	def build(self):
		return presentation

if __name__ == "__main__":
	GomokuApp().run()