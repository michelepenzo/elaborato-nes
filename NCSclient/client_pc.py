#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Client():
	#Create socket object
	cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# using IP address i'm able to connect from app
	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')  # local ip
	port = 5050

	cs.connect((host, port)) 

	while True:
		mouse_x, mouse_y = pyautogui.position()
		cs.send(bytes( '0#' + str(mouse_x) + '#' + str(mouse_y) + '#', 'ascii'))
		# send all	

	cs.close()

if __name__ == '__main__':
	Client()
