#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#This option allows the port to be reused before the timeout_wait expires on connections
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
# while 1:
#     data = conn.recv(BUFFER_SIZE)
#     if not data: break
#     print "received data:", data
#     conn.send(data)  # echo
conn.send('Test Message!')  # echo
#conn.shutdown(SHUT_RDWR)
conn.close()
