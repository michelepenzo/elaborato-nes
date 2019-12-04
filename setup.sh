#!/usr/bin/bash

__author__='Michele Penzo'

# Primo pacchetto
dpkg -s "python3-pip" &> /dev/null

if [ $? -eq 0 ]; then
    :
else
    sudo apt-get install python3-pip
fi

# Secondo pacchetto

dpkg -s "python3-tk" &> /dev/null

if [ $? -eq 0 ]; then
    :
else
    sudo apt-get install python3-tk
fi

# Terzo pacchetto
dpkg -s "python3-dev" &> /dev/null

if [ $? -eq 0 ]; then
    :
else
    sudo apt-get install python3-dev
    pip3 install pyautogui
fi

# Esecuzione su due terminali dei programmi

#konsole -e python3 $(pwd)/NCSserver/paint.py &
#konsole -e python3 $(pwd)/NCSserver/server.py

#exit