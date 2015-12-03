class Spectator(object):
	"""docstring for Spectator"""
	def __init__(self):
		super(Spectator, self).__init__()
		self.playerList = []

	def getSpectatorList(self):
		return self.playerList

	def addPlayerToSpectatorList(self, player):
		self.playerList.append(player)

	def deletePlayerFromSpectatorList(self, player):
		if player in self.playerList
			self.playerList.remove(player)