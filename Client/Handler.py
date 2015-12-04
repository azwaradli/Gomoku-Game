import json
import standard

class Handler(object):
	listRooms = ["" for j in range(5)]
	def __init__(self, conn):
		self.conn = conn
		self.running = True
		self.msgRecv = ""
		self.playerId = -1
		self.roomId = -1
		self.message = ""

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
				else:
					print "login unsuccessful..."

			elif message[standard.MESSAGE] == standard.MESSAGE_REFRESH:
				i = 0
				for room in message["room_list"]:
					self.listRooms[i] = room
					i += 1
					print room

			elif message[standard.MESSAGE] == standard.MESSAGE_CREATE_ROOM:
				if message[standard.MESSAGE_SUCCESS] == 1:
					print "create room successful."
				else:
					print "create room unsuccessful..."

			elif message[standard.MESSAGE] == "list_user":
				for player in message["player_list"]:
					print player

			elif message[standard.MESSAGE] == standard.MESSAGE_JOIN_ROOM:
				if message[standard.MESSAGE_SUCCESS] == 1:
					self.room_id = message[standard.PARAM_ROOM_ID]
					print "you are connected to room", self.room_id
				else:
					print "login unsuccessful..."

			self.message = message

