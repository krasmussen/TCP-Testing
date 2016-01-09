#!/usr/bin/env python

# import socket
# 
# 
# TCP_IP = '127.0.0.1'
# TCP_PORT = 9999
# BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!"
# 
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
# s.send(MESSAGE)
# data = s.recv(BUFFER_SIZE)
# s.close()
# 
# print "received data:", data



#Connect to server
#Register identity
#Send outstanding results from completed commands
#Listen for instructions


import sys
import socket
import fcntl, os
import errno
import pdb
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:

    if not s:       #If no open socket, open one
        try:
            s.connect(('127.0.0.1',9999))
        except:
            print "Failure!"
            sys.exit(1)
        else:
            s.setblocking(0)
            s.getpeername()
#What does s get set to if the open fails?

    pdb.set_trace()

    try:
        msg = s.recv(4096)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            print "Continued!"
            continue
        else:
            # a "real" error occurred
            print "Error!"
            print e
            sys.exit(1)
    except Exception as e:
        print "Error 2!"
        print e
    else:
        # got a message, do something :)
        if msg:
#        if ( len(msg) > 0):
            print "received data:", msg
#        sys.exit(0)


#If not connected to server, try to connect
    #Upon connection, register identity
    #Send outstanding results from completed commands
    #Reply based on last msg reported by server, not based on last one we sent
        #In case the server lost the data
#Check for input on the socket

#Thread B:
#Check scheduler
#Execute scheduled tasks
    #Store results and send them
#If the server connection goes down, change the state to reconnect

#Sublime Text Editor
#Multiprocessing library
#    Uses queue for inter-process comms
#scapy - Python IP packet builder
#http://stackoverflow.com/questions/5686490/detect-socket-hangup-without-sending-or-receiving
