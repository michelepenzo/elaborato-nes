# Sistemi Embedded di Rete

Esmpio di NCS, svolto come progetto per il corso NES. <br>

## Prerequisiti

- Server:
	- SO Linux <br>
	- python 3.7
- Client:
	- Smartphone Android _oppure_<br>
	- SO Linux con python 3.7
- Dispositivi connessi alla stessa rete WiFi. <br>

## Funzionamento
1. Clonare la repository:
```
git clone https://github.com/michelepenzo/elaborato-nes.git
```

2. Eseguire il file per installare i pacchetti necessari:
```
cd elaborato-nes
./setup.sh
```

3. Eseguire il __server__ guardando il valore dell'indirizzo IP.
```
python3 NCSserver/server.py
```

4. Per il __client__:
	- da *smartphone Android* installare il file ``client_app.apk`` che si trova in ``NCSclient_interface``, aprirlo e inserire l'indirizzo IP ottenuto dal server.
	- da *PC* aprire un terminale ed eseguire:
		```
		cd NCSclient_interface
		python3 client_pc.py
		```

5. Eseguire l'applicazione interattiva:
```
python3 circle_gui.py
```


## Licenza
Consultare il file [LICENSE](https://github.com/michelepenzo/nes/blob/master/LICENSE) nella repo.

### Contatti
[Telegram](https://t.me/michelepenzo)