class Spectator(object):
	"""docstring for Spectator"""
	def __init__(self):
		super(Spectator, self).__init__()
		self.player_list = []

	def getSpectatorList(self):
		return self.player_list

	def addPlayerToSpectatorList(self, player):
		self.player_list.append(player)

	def deletePlayerFromSpectatorList(self, player):
		if player in self.player_list
			self.player_list.remove(player)