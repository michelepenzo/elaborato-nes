#!/usr/bin/python3
# coding=utf-8

__author__ = 'Michele Penzo'
__version__ = '1.0'

import socket

def get_data():
	host = 'localhost'        
	port = 9900     

	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind((host, port))

	socket.listen(1)
	print("Started server! listeing to {}:{}".format(host, port))
	socket.accept()
	print('Connected by', addr)

	while True:
	    try:
	        data = conn.recv(1024)
	        if not data:
	        	break
	        
	        print ("ricevuto" + str(data))
	        conn.sendall(str.encode("SERVER_RES: " + str(data)))

	    except socket.error:
	        print ("Error Occured.")
	        break

	conn.close()

if __name__ == '__main__':
    print('start')
    get_data()
    # lsof -n -i
