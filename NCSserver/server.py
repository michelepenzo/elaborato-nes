#!/usr/bin/python3
# coding=utf-8

__author__ = 'Michele Penzo'
__version__ = '1.0'

import socket
import netifaces as ni

def get_data():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create socket

	host =  socket.gethostbyname( socket.gethostname() )  # get my IP
	host = '192.168.1.9'
	port = 0	# first free port

	s.bind((host, port))

	s.listen(1)
	print("Started server!\nListeing to {}:{}".format(host, s.getsockname()[1] ))
	conn, addr = s.accept()
	print('Device connected:', addr)	
	while True:

	    try:
	        data = conn.recv(1024)
	        if not data: break
	        print ("Client Says: " + str(data))
	        conn.sendall(str.encode("SERVER_RES: " + str(data)))
	    except socket.error:
	        print ("Error Occured.")
	        break

	conn.close()


if __name__ == '__main__':
    get_data()
    # lsof -n -i