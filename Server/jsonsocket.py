import json, socket, struct

class JsonSocket(object):
	"""docstring for JsonSocket"""
	def __init__(self, address='127.0.0.1', port="3423"):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn = self.socket
		self._addr = address
		self._port = port

	def sendObj(self, obj):
		msg = json.dumps(obj)
		if self.socket:
			frmt = "=%ds" % len(msg)
			packedMsg = struct.pack(frmt, msg)
			packedHdr = struct.pack
		