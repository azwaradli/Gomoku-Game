from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import Property, NumericProperty,\
    ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class GomokuLogin(Screen):
	pass

class GomokuRooms(Screen):
	username = Property('')

	def setUsername(self, user):
		self.username = user

	def setRoomAmount(self, amount):
		self.roomAmount = amount

	def printRoom(self):
		roomAmount = 0
		if roomAmount > 0:
			for i in range (0,roomAmount):
				#Init
				roomName = Label(text="Room 1")
				tag1 = Label(text="Player :")

				#Process
				titleGrid = GridLayout(rows=3, padding=[5,10])
				titleGrid.add_widget(roomName)
				titleGrid.add_widget(GridLayout())
				titleGrid.add_widget(GridLayout())
				playerGrid = GridLayout(rows=4, padding=[5,10])
				playerGrid.add_widget(tag1)
				playerGrid.add_widget(Label(text='fauzan'))
				playerGrid.add_widget(Label(text='ahmad'))
				playerGrid.add_widget(Label(text='azwar'))

				#Render
				self.ids.rooms.add_widget(titleGrid)
				self.ids.rooms.add_widget(playerGrid)
		else:
			self.ids.rooms.add_widget(Label(text="No rooms available"))

class ScreenManager(ScreenManager):
	pass

class GomokuRoom(Widget):
	pass

presentation = Builder.load_file("gomoku.kv")

class GomokuApp(App):

	def build(self):
		return presentation

if __name__ == "__main__":
	GomokuApp().run()