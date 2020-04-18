#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Client():
	#Create socket object
	clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# using IP address i'm able to connect from app
	host = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode('ascii').replace('\n','').replace(' ','')  # local ip
	port = 5050

	clientsocket.connect((host, port)) 
	
	'''
	message = clientsocket.recv(1024)
	clientsocket.close()
	print(message.decode('ascii'))
	'''

	# qui devo leggere i valori del mouse e inviarli in base a come li riceve il server
	# send byte
	clientsocket.send()

if __name__ == '__main__':
	Client()
