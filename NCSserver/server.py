#!/usr/bin/python3

__author__ = 'Michele Penzo'
__version__ = '1.0'

import socket
import subprocess
import pyautogui

def Server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create socket

	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')
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

	        data = conn.recv(1024)
	        if not data:
	        	print('no data')
	        	break

	        cmd=str(data.decode('ascii')).split('#')
	        
	        if cmd[0] is '0':	# action down
	        	pyautogui.click(int(cmd[1]), int(cmd[2]))
	        	print('0')
	        else:	# action move
	        	pyautogui.click(int(cmd[1]), int(cmd[2]))
	        	print('1')
	   
	        conn.sendall(str.encode("SERVER_RES: " + str(data)))

	    except socket.error:
	        print ("Error Occured.")
	        break

	conn.close()


if __name__ == '__main__':
    Server()