import json

class MessageController(object):
	"""docstring for MessageController"""
	def __init__(self):
		super(MessageController, self).__init__()

	def parseToDict(self, message):
		data = json.loads(message)
		return dict(data)

	def compileToJSON(self, dictionary):
		obj = json.dumps(dictionary)
		return obj

	def recv(self, sockfd, size):
		data = ''
        while len(data) < size:
            dataTmp = sockfd.recv(size-len(data))
            data += dataTmp
            if dataTmp == '':
                raise RuntimeError("Socket connection broken")

        return data
		
	def send(self, sockfd, data):
		sent = 0
		    while sent < len(data):
		    	sent += sockfd.send(data[sent:])

	def sendMessage(self, sockfd, data):
		msg = json.dumps(data)
        if sockfd:
            frmt = "=%ds" % len(msg)
            packedMsg = struct.pack(frmt, msg)
            packedHdr = struct.pack('=I', len(packedMsg))
 
            self.send(sockfd, packedHdr)
            self.send(sockfd, packedMsg)

    def receiveMessage(self, sockfd):
    	data = self.recv(BUF_MAX)
        frmt = "=%ds" % BUF_MAX
        msg = struct.unpack(frmt, data)
        return json.loads(msg[0])

	def broadcastAll(self, message):
		pass

	def broadcastRoom(self, message, room_id):
		pass

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