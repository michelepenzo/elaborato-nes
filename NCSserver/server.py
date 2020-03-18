#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Server():

	# valori dello schermo
	MAX_SIZE_X, MAX_SIZE_Y = pyautogui.size()

	# valori iniziali di x e y
	x, y = 0, 0
	move_x, move_y = 0, 0
	offset_x, offset_y = 0, 0

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create socket

	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')  # stampo l'indirzzo ip locale
	port = 0    # free port

	s.bind((host, port))

	s.listen(1)

	print('IP address: '+ str(host))
	print('Port: '+ str(s.getsockname()[1]))

	conn, addr = s.accept()
	print('Device connected')   

	cmd = list()
	pyautogui.FAILSAFE = False
	while True:
		try:

			data = conn.recv(1024)  # ricevo il dato dall'app
			if not data:
				print('no data')
				break

			cmd=str(data.decode('ascii')).split('#')    # splitto per vedere il comando che voglio utilizzare
			
			x, y = int(cmd[1]), int(cmd[2])
			
			if cmd[0] is '0':   # initial press
				mouse_x, mouse_y = pyautogui.position()
				offset_x, offset_y = x, y
			
			elif cmd[0] is '1': # moving around
				move_x = mouse_x + (x - offset_x) 
				move_y = mouse_y + (y - offset_y)
				pyautogui.dragTo(move_x, move_y, button='left') 
				#pyautogui.moveTo(move_x, move_y)
			
			elif cmd[0] is '2':
				pyautogui.click(pyautogui.position(), button='left')
			
			elif cmd[0] is '3':
				pyautogui.click(pyautogui.position(), button='right')
			
			else:
				print('Bad command')

			conn.sendall(str.encode("SERVER_RES: " + str(data)))
			
		except (socket.error, KeyboardInterrupt) as e:
			print ("\nError Occured.")
			break

	conn.close()


if __name__ == '__main__':
	Server()
