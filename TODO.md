# TODO list file

## README
- aggiungere l'apk e fare la release

## SERVER
- torna al punto in basso ogni volta che alzo il dito

## CLIENT
- settare valore IP

-------------------------------------------------------------------------------------------------
## APPUNTI
sudo tc qdisc add dev wlp0s20f3 root netem delay 1000ms ----> 

sudo tcpdump -c 50 -tttt -i wlp0s20f3 ----> cattura un numero specifico di pacchetti provenienti da una determinata interfaccia

sudo tcpdump -i wlp0s20f3 tcp ----> cattura solamente i pacchetti tcp

sudo tcpdump -i wlp0s20f3 port 51777 ----> catturra i pacchetti solamente su quella porta

sudo tc qdisc add dev wlp0s20f3 root netem loss 0.1%