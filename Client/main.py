from Connection import *
from client import *

if __name__ == '__main__':
	host = "127.0.0.1"
	port = 5000

	client = Client(Connection(host,port))

	client.handler()
