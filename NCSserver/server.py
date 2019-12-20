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

	# valori usati per interpolare i punti, salvo con i valori attuali
	x2, y2 = x1, y1 

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

			# interpolazione dei punti in quanto i valori sono discontinui, quindi quando vado a disegnare non faccio delle linee ma solamente dei punti
			print('MOVE --- x: ' + str(x1)+' ---- y :'+ str(y1))



			# faccio la differenza dei valori e muovo
			pyautogui.drag(x1.x2, 0, button='left')
			pyautogui.drag(0, y1-y2, button='left')
		

			'''
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
			'''
			conn.sendall(str.encode("SERVER_RES: " + str(data)))

			x2, y2 = x1, y1

		except socket.error:
			print ("Error Occured.")
			break

	conn.close()


if __name__ == '__main__':
	Server()
