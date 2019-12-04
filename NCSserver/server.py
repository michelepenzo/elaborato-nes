#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Server():

	# valori dello schermo
	MAX_SIZE_X, MAX_SIZE_Y = pyautogui.size()

	# valori iniziali di x e y
	x, y = pyautogui.position()

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
			
			if cmd[0] is '0':
				# action down
				x,y = int(cmd[1]), int(cmd[2])
				pyautogui.moveTo(x, y)
				print('MOVE --- x: ' + str(x)+' ---- y :'+ str(y))

			elif cmd[0] is '1':
				# action move
				x,y = int(cmd[1]), int(cmd[2])
				pyautogui.dragTo(x, y, button='left')
				#pyautogui.moveTo(x, y)
				print('DRAG --- x: ' + str(x)+' ---- y :'+ str(y))

			elif cmd[0] is '2':
				pyautogui.click(x, y)
				print('LEFT --- x: ' + str(x)+' ---- y :'+ str(y))  

			elif cmd[0] is '3':
				pyautogui.click(x, y, button='right')
				print('RIGHT --- x: ' + str(x)+' ---- y :'+ str(y))             

			conn.sendall(str.encode("SERVER_RES: " + str(data)))

		except socket.error:
			print ("Error Occured.")
			break

	conn.close()


if __name__ == '__main__':
	Server()
