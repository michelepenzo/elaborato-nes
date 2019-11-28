#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui


def Server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create socket

	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')	# stampo l'indirzzo ip locale
	port = 0	# free port

	s.bind((host, port))

	s.listen(1)

	print('IP address: '+ str(host))
	print('Port: '+ str(s.getsockname()[1]))

	conn, addr = s.accept()
	print('Device connected')	

	cmd = list()

	while True:
	    try:

	        data = conn.recv(1024)	# ricevo il dato dall'app
	        if not data:
	        	print('no data')
	        	break

	        cmd=str(data.decode('ascii')).split('#')	# splitto per vedere il comando che voglio utilizzare
	        
	        # ricevo i dati e mi muovo all'interno della grafica
	        if cmd[0] is '0':	# solo movimento
	        	pyautogui.moveTo(int(cmd[1]), int(cmd[2]))
	        else:	# action scrittura
	        	pyautogui.click(int(cmd[1]), int(cmd[2]), button='left')	# TODO
	   
	        conn.sendall(str.encode("SERVER_RES: " + str(data)))

	    except socket.error:
	        print ("Error Occured.")
	        break

	conn.close()


if __name__ == '__main__':
    Server()
