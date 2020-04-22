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

	# CLIENT_PC
	msg = 'pc' + (' '*1024)
	msg = msg[:1024].encode('ascii')
	cs.send(msg)

	# starting point
	msg = '0#0#0' + (' '*1024)
	msg = msg[:1024].encode('ascii')
	cs.send(msg)
	
	old_x, old_y = 0, 0

	while True:
		try:	
			mouse_x, mouse_y = pyautogui.position()

			if not( mouse_x == old_x and mouse_y == old_y):
				msg = '1#' + str(mouse_x) + '#' + str(mouse_y) + '#' + (' '*1024)
				# there isn't flush method in python3
				msg = msg[:1024].encode('ascii')			
				
				cs.send(msg)

				old_x, old_y = mouse_x, mouse_y

		except (socket.error, KeyboardInterrupt, OSError) as e:
			print ("\nError Occured.")
			conn.close()
			break


if __name__ == '__main__':
	Client()
