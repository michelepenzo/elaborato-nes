#!/usr/bin/python3

__author__ = 'Michele Penzo'
__version__ = '1.0'

import socket
import subprocess

def get_data():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create socket

	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')
	port = 0	# free port

	s.bind((host, port))

	s.listen(1)
	print("Started server!\nListeing to {}:{}".format(host, s.getsockname()[1] ))
	conn, addr = s.accept()
	print('Device connected')	
	while True:

	    try:
	        data = conn.recv(1024)
	        if not data:
	        	print('no data')
	        	break

	        print (str(data.decode('ascii')))

	        # TODO : parserizzare i file con switch, se 1 .., se 2..., ecc

	        conn.sendall(str.encode("SERVER_RES: " + str(data)))
	    except socket.error:
	        print ("Error Occured.")
	        break

	conn.close()


if __name__ == '__main__':
    get_data()
    # lsof -n -i