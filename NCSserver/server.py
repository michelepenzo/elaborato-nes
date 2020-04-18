#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui
from time import sleep
from random import uniform

def Server():

	# max size screen
	MAX_SIZE_X, MAX_SIZE_Y = pyautogui.size()
	
	# -------------------
	# ---- max delay ----
	MAX_DELAY = 0.4

	# starting values
	x, y = 0, 0
	move_x, move_y = 0, 0
	offset_x, offset_y = 0, 0
	old_cmd = '0'

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # open socket

	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')  # local ip
	port = 5050	 # static port

	s.bind((host, port))

	s.listen(1)

	print('IP address: '+ str(host))
	#print('Port: '+ str(s.getsockname()[1]))

	conn, addr = s.accept()
	print('Device connected')   

	cmd = list()
	pyautogui.FAILSAFE = False

	while True:
		try:

			data = conn.recv(1024)  # get data
			if not data:
				print('no data')
				break

			cmd=str(data.decode('ascii')).split('#')	# split command 
			x, y = int(cmd[1]), int(cmd[2])				# get position
			
			# -------------------
			# ------ delay ------
			sleep( uniform(0.1, MAX_DELAY) )	# milliseconds
			

			if cmd[0] is '0':   # initial press
				mouse_x, mouse_y = pyautogui.position()
				offset_x, offset_y = x, y
				old_cmd = '0'
				
			elif cmd[0] is '1':	# simple movement
				
				if old_cmd is '4':
					move_x = mouse_x + (x - offset_x) 
					move_y = mouse_y + (y - offset_y)
					pyautogui.dragTo(move_x, move_y)
					old_cmd = '4'

				else:
					move_x = mouse_x + (x - offset_x) 
					move_y = mouse_y + (y - offset_y)
					pyautogui.moveTo(move_x, move_y)
					old_cmd = '1'
				'''
				elif cmd[0] is '2':	# button left
					pyautogui.click(pyautogui.position(), button='left')
					old_cmd = '2'
				
				elif cmd[0] is '3':	# button right
					pyautogui.click(pyautogui.position(), button='right')
					old_cmd = '3'
				'''
			elif cmd[0] is '4':	# double tap and left button clicked
				pyautogui.click(pyautogui.position(), clicks=2, button='left')
				old_cmd = '4'
			
			else:
				print('Bad command')

			#conn.sendall(str.encode("SERVER_RES: " + str(data)))
			
		except (socket.error, KeyboardInterrupt) as e:
			print ("\nError Occured.")
			conn.close()
			break

	conn.close()

if __name__ == '__main__':
	Server()
