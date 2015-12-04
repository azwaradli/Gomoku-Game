import json

class MessageController(object):
	"""docstring for MessageController"""
	def __init__(self):
		super(MessageController, self).__init__()

	def sendMessage(self, sockfd, data):
		try:
			serialized = json.dumps(data)
		except (TypeError, ValueError), e:
			raise Exception("You can only send JSON-serializable data")
		# send the length of the serialized data first
		sockfd.send('%d\n' % len(serialized))
		# send the serialized data
		sockfd.sendall(serialized)

	def receiveMessage(self, sockfd):
		lengthStr = ''
		char = sockfd.recv(1)
		while char != '\n':
			lengthStr += char
			char = sockfd.recv(1)
		total = int(lengthStr)

		# use a memoryview to receive the data chunk by chunk efficiently
		view = memoryview(bytearray(total))
		nextOffset = 0
		while total - nextOffset > 0:
			recv_size = sockfd.recv_into(view[nextOffset:], total - nextOffset)
			nextOffset += recv_size

		try:
			deserialized = json.loads(view.tobytes())
		except (TypeError, ValueError), e:
			raise Exception('Data received was not in JSON format')

		print deserialized
		return deserialized

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