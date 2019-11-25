#!/usr/bin/python3

__author__ = 'Michele Penzo'
__version__ = '1.0'

from paint import *
from server import *

if __name__ == '__main__':
    # eseguire entrambi i moduli python, se il server crasha allora deve essere chiuso anche paint
    Server()
    Paint()