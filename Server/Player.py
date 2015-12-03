class Player(object):
	def __init__(self, p_id, p_name, sock_fd):
		super(Player, self).__init__()
		self.id = p_id
		self.sockfd = sock_fd		# socket descriptor of the player client
		self.nickname = p_name		# nickname of player (shown on game)
		self.pawn = 0

	def getPlayerId(self):
		return self.id

	def getPlayerSocket(self):
		return self.sockfd

	def getPawn(self):
		return self.pawn

	def getPlayerNickname(self):
		return self.nickname

	def setPlayerNickname(self, _name):
		self.nickname = _name

	def setPawn(self, _pawn):
		self.pawn = _pawn