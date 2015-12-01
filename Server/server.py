import socket, select

def broadcast_data(sock, message):
	for socket in CONNECTION_LIST:
		if socket != servsock:
			try:
				socket.send(message)
			except :
				socket.close()
				CONNECTION_LIST.remove(sock)

def print_matrix(matrix):
	result = ""
	for i in range(5):
		result += str(matrix[i]) + '\n'

	return result


if __name__ == "__main__":

	CONNECTION_LIST = []	# list of socket clients
	RECV_BUF = 4096
	PORT = 5000
	IP_ADDR = "0.0.0.0"

	matrix = [[0] * 20 for i in range(20)]

	servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servsock.bind((IP_ADDR, PORT))
	servsock.listen(10)

	CONNECTION_LIST.append(servsock)

	print "Chat server started on port " + str(PORT)

	while 1:
		readsock, writesock, errsock = select.select(CONNECTION_LIST, [], [])

		for sock in readsock:
			if sock == servsock:
				sockfd, addr = servsock.accept()
				CONNECTION_LIST.append(sockfd)
				print "Client (%s, %s) connected!" % addr
				broadcast_data(sockfd, "[%s:%s] Has entered the room\n" % addr)
				broadcast_data(sockfd, print_matrix(matrix))

			else:
				try:
					data = sock.recv(RECV_BUF)
					if data:
						coordinate = data.split('|')
						print coordinate[0], coordinate[1]
						matrix[int(coordinate[0])][int(coordinate[1])] = 1
						broadcast_data(sockfd, print_matrix(matrix))

				except:
					if sock in CONNECTION_LIST:
						CONNECTION_LIST.remove(sock)
					broadcast_data(sock, "Client (%s, %s) is offline!" % addr)
					
					sock.close()
					
					continue

	servsock.close()
				