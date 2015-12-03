import socket, select

class Connection(object):

	def __init__(self, host, port, buf_size = 4096):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.buf_size = buf_size
		self.socket.connect((self.socket, self.port))
		self.socket.blocking(0)
		self.CONNECT = True

	def send(self, data):
		if not self.socket:
			raise Exception("You have to connect first before sending data")
		_send(self.socket, data)
		return self

	def recv(self):
		if not self.socket:
			raise Exception("You have to connect first before receiving data")
		return _recv(self.socket)

	def recv_and_close(self):
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
	#read the length of the data, letter by letter untuk we reach EOL
	lengthStr = ''
	char = socket.recv(1)
	while char != '\n':
		lengthStr += char
		char = socket.recv(1)
	total = int(length_str)
	# use a memoryview to receive the data chunk by chunk efficiently
	view = memoryview(bytearray(total))
	next_offset = 0
	while total - next_offset > 0:
		recv_size = socket.recv_into(view[next_offset:], total - next_offset)
		next_offset += recv_size
	try:
		deserialized = json.loads(view.tobytes())
	except (TypeError, ValueError), e:
		raise Exception('Data received was not in JSON format')
	return deserialized
