import socket, select, json

class Connection(object):

	def __init__(self, host, port, bufSize = 4096):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.bufSize = bufSize
		self.socket.connect((self.host, self.port))
		self.CONNECT = True

	def getSocket(self):
		return self.socket

	def send(self, data):
		if not self.socket:
			raise Exception("You have to connect first before sending data")
		_send(self.socket, data)
		return self

	def recv(self):
		if not self.socket:
			raise Exception("You have to connect first before receiving data")
		return _recv(self.socket)

	def recvAndClose(self):
		data = self.recv()
		self.close()
		return data

	def close(self):
		if self.socket:
			self.socket.close()
			self.socket = None

# helper function
def _send(socket, data):
	try:
		serialized = json.dumps(data)
	except (TypeError, ValueError), e:
		raise Exception("You can only send JSON-serializable data")
	# send the length of the serialized data first
	socket.send('%d\n' % len(serialized))
	# send the serialized data
	socket.sendall(serialized)

def _recv(socket):
	lengthStr = ''
	char = socket.recv(1)
	while char != '\n':
		lengthStr += char
		char = socket.recv(1)
	total = int(lengthStr)
	# use a memoryview to receive the data chunk by chunk efficiently
	view = memoryview(bytearray(total))
	nextOffset = 0
	while total - nextOffset > 0:
		recv_size = socket.recv_into(view[nextOffset:], total - nextOffset)
		nextOffset += recv_size
	try:
		deserialized = json.loads(view.tobytes())
	except (TypeError, ValueError), e:
		raise Exception('Data received was not in JSON format')

	return deserialized
