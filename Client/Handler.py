import json
import standard

class Handler(object):
	listRooms = []
	def __init__(self, conn):
		self.conn = conn
		self.running = True
		self.msgRecv = ""
		self.playerId = -1
		self.roomId = -1
		self.message = ""
		self.receiveRoomEvent = []
		self.receiveLoginEvent = []

	def getRooms(self):
		return self.listRooms

	def handle(self):
		while True:
			try:
				self.msgRecv = self.conn.recv() # return in JSON format
				if not self.msgRecv:
					if not sockReadReady:
						self.conn.close()
						self.running = False

				self.processDataRecv(self.msgRecv)
			except Exception, e:
				print e

	def processDataRecv(self, message):
		if standard.MESSAGE not in message:
			return

		else:
			if message[standard.MESSAGE] == standard.MESSAGE_AUTH:
				if message[standard.MESSAGE_SUCCESS] == 1:
					self.player_id = message[standard.PARAM_PLAYER_ID]
					print "login successful. your login key =", self.player_id
					for callback in self.receiveLoginEvent:
						print "announcing login callback"
						callback(self.player_id)
				else:
					print "login unsuccessful..."

			elif message[standard.MESSAGE] == standard.MESSAGE_REFRESH:
				i = 0
				del self.listRooms [:]
				for room in message[standard.PARAM_ROOM_LIST]:
					self.listRooms.append(room)
					i += 1
					for callback in self.receiveRoomEvent:
						print "announcing rooms callback"
						callback(self.listRooms)

			elif message[standard.MESSAGE] == standard.MESSAGE_CREATE_ROOM:
				if message[standard.MESSAGE_SUCCESS] == 1:
					print "create room successful."
				else:
					print "create room unsuccessful..."

			elif message[standard.MESSAGE] == standard.MESSAGE_JOIN_ROOM:
				if message[standard.MESSAGE_SUCCESS] == 1:
					self.room_id = message[standard.PARAM_ROOM_ID]

					roomName = message[standard.PARAM_ROOM_NAME]
					playerList = message[standard.PARAM_ROOM_PLAYERS]
					
					print "you are connected to room", self.room_id
				else:
					print "room join unsuccessful..."

			elif message[standard.MESSAGE] == standard.MESSAGE_JOIN_GAME:
				if message[standard.MESSAGE_SUCCESS] == 1:
					print "you are connected to the game"
				else:
					print "join game unsuccessful..."

			self.message = message

	def whenRoomReceived(self, callback):
		print 'room'
		self.receiveRoomEvent.append(callback)

	def whenLoginReceived(self,callback):
		print 'login'
		self.receiveLoginEvent.append(callback)











