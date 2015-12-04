from Serv import *

if __name__ == '__main__':
	try:
		Server().serverListen()
	except KeyboardInterrupt:
		print "KeyboardInterrupt: Terminated by User"
		exit()