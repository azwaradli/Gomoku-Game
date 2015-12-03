import json

class MessageController(object):
	"""docstring for MessageController"""
	def __init__(self):
		super(MessageController, self).__init__()

	def sendMessage(self, sockfd, data):
		msg = json.dumps(data)
		sockfd.sendall(msg + "\n")

	def receiveMessage(self, sockfd):
		data = sockfd.recv(BUF_MAX)
		msg = data.split("\n")

		message = json.loads(msg[0])
		return message

	BUF_MAX = 4096
		

# MESSAGE CONTROLLER TEST ONLY

def main():
	mc = MessageController()

	obj = "{ \"message\": \"select\", \"return\": 0}"
	parsed = mc.parseToDict(obj)
	print parsed

	print parsed['message']

	print mc.compileToJSON(parsed)

if __name__ == '__main__':
	main()