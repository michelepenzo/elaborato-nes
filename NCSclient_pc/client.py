#!/usr/bin/python3

__author__ = 'Michele Penzo'

import socket
import subprocess
import pyautogui

def Client():
	#Create socket object
	clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# TODO modificare qui perchè forse non va bene localhost
	ip = 'localhost'
	#ip = input('Insert server IP address: ').replace('\n','')
	port = 5050

	clientsocket.connect((ip, port)) 
	
	'''
	message = clientsocket.recv(1024)
	clientsocket.close()
	print(message.decode('ascii'))
	'''

	# qui devo leggere i valori del mouse e inviarli in base a come li riceve il server
	clientsocket.send()

if __name__ == '__main__':
	Client()
