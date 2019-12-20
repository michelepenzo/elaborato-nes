#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Server():

	# valori dello schermo
	MAX_SIZE_X, MAX_SIZE_Y = pyautogui.size()

	# valori iniziali di x e y
	x1, y1 = pyautogui.position()

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
			
			x1, y1 = int(cmd[1]), int(cmd[2])

			print('x1: ' + str(x1)+' ---- y1 :'+ str(y1))

			if cmd[0] is '0':	# action down
				pyautogui.moveTo(x1, y1)
			
			elif cmd[0] is '1':	# action move
				pyautogui.dragTo(x1, y1, button='left')
				
			elif cmd[0] is '2':
				pyautogui.click(x1, y1, button='left')
				
			elif cmd[0] is '3':
				pyautogui.click(x1, y1, button='right')
			
			conn.sendall(str.encode("SERVER_RES: " + str(data)))

		except socket.error:
			print ("Error Occured.")
			break

	conn.close()


if __name__ == '__main__':
	Server()
