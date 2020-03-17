#!/usr/bin/python3

__author__ = 'Michele Penzo'

import os		# ritardare il traffico
import time		# aspettare un po

'''
Vedere i 50 pacchetti in arrivo su quella interfacci
a 
udo tcpdump -c 50 -tttt -i wlp0s20f3

'''

def Guasta():

	# TODO interfaccia da riga di comando
	interface = 'wlp0s20f3'

	while True:
		os.system('sudo tc qdisc add dev ' + interface +' root netem delay 1000ms')
		#time.sleep(1)
	

if __name__ == '__main__':
	Guasta()


