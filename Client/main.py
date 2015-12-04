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

from client import Client
from Connection import Connection
from Handler import Handler
import thread

#Global Variable
connected = False
try:
	client =  Client(Connection("127.0.0.1", 5000))
	handler = Handler(Connection("127.0.0.1", 5000))
	connected = True
except:
	connected = False

#Function for changing the screen
def game_screen(*args):
	App.get_running_app().root.get_screen('game').init()
	App.get_running_app().root.current = 'game'

class GomokuLogin(Screen):
	def login(self, user):
		if user:
			App.get_running_app().root.get_screen('room').setUsername(user)
			client.login(user)
			App.get_running_app().root.current = 'room'
		else:
			App.get_running_app().root.current = 'login'

class GomokuRooms(Screen):
	username = Property('')

	def setUsername(self, user):
		self.username = user

	def getUsername(self):
		return username

	def setRoomAmount(self, amount):
		self.roomAmount = amount

	def printRoom(self):
		roomAmount = 0
		self.ids.rooms.clear_widgets()
		if roomAmount > 0:
			for i in range (0,roomAmount):
				#Init
				roomName = Label(text="[color=F41D4E]Room 1[/color]", markup= True, font_size='20sp')
				tag1 = Label(text="[color=ffffff]Player[/color]", markup=True)
				mainGrid = GridLayout(cols= 2)

				#Setting Background - not function yet -
				#if i == 0:
				#	mainGrid.canvas.add(Color(0.06,0.537,0.98,1))
				#	mainGrid.canvas.add(Rectangle(pos=self.pos, size=self.size))

				#Process
					#adding roomname
				titleGrid = GridLayout(rows=2, padding=[5,10])
				titleGrid.add_widget(roomName)
					#adding button for room
				buttonGrid = GridLayout(rows=2, padding=[250,0])
				joinButton = Button(text='[color=F41D4E]Join[/color]',on_press= game_screen, markup= True, background_color=[2.8,2.8,2.8,1])
				#joinButton.bind(on_press=change_screen('game'))
				watchButton = Button(text='[color=F41D4E]Watch[/color]', markup= True, background_color=[2.8,2.8,2.8,1])
				buttonGrid.add_widget(joinButton)
				buttonGrid.add_widget(watchButton)

				titleGrid.add_widget(buttonGrid)
					#adding playername
				playerGrid = GridLayout(rows=2, padding=[100,0])
				playerGrid.add_widget(tag1)

				playerGridInner = GridLayout(cols=2)
				playerGridInner.add_widget(Button(text='[color=eeeeee]fauzan[/color]', markup=True, background_color=[2.953,1.67,0.471,1]))
				playerGridInner.add_widget(Button(text='[color=eeeeee]ahmad[/color]', markup=True, background_color=[2.953,1.67,0.471,1]))
				playerGridInner.add_widget(Button(text='[color=eeeeee]azwar[/color]', markup=True, background_color=[2.953,1.67,0.471,1]))
				playerGridInner.add_widget(Button(text='[color=eeeeee]adli[/color]', markup=True, background_color=[2.953,1.67,0.471,1]))
				playerGridInner.add_widget(Button(text='[color=eeeeee]naufal[/color]', markup=True, background_color=[2.953,1.67,0.471,1]))

				playerGrid.add_widget(playerGridInner)
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
	gameboard = [[Button() for j in range(20)] for i in range(20)]
	def init(self):
		p = 0
		for row in self.gameboard:
			q = 0
			for square in row:
				temp = str(p)
				temp += "-"
				temp += str(q)
				square = Button(text=temp)
				square.bind(on_press= self.game_button_event)
				q += 1
		p += 1
		self.printBoard()
	def printBoard(self):
		self.ids.game_board.clear_widgets()
		for row in self.gameboard:
			for square in row:
				self.ids.game_board.add_widget(square)
	def updateBoard(self, row, col, color):
		gameboard[row][col] = Button(text='X', background_color=color)
		printBoard()

	def game_button_event(self, *args):
		ids = button.text.split(',')
		id1 = int(ids[0])
		id2 = int(ids[1])
		user = App.get_running_app().root.get_screen('room').getUsername()
		color = Color(rgba(0,0,0,1))
		updateBoard(id1, id2, color)


class ScreenManager(ScreenManager):
	pass

presentation = Builder.load_file("gomoku.kv")
failed = Builder.load_file("failed.kv")

class GomokuApp(App):

	def build(self):
		try:
			thread.start_new_thread(handler.handle, ("Thread-1", 2, ))
		except:
			return failed
		if not connected:
			return failed
		return presentation

if __name__ == "__main__":
	GomokuApp().run()