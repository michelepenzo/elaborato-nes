# Sistemi Embedded di Rete

Esmpio di NCS, svolto come progetto per il corso NES. <br>

## Prerequisiti

- Server:
	- SO Linux (sviluppato e testato su Ubuntu 19.10) <br>
	- python 3.7
- Client: Smartphone Android <br>
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


3. Eseguire il __server__ guardando i valori dell'indirizzo IP e della porta.
```
python3 NCSserver/server.py
```

4. Per il __client__ installare il file ``NCS-client.apk``, aprirlo e inserire i valori ottenuti dal server.


## Licenza
Consultare il file [LICENSE](https://github.com/michelepenzo/nes/blob/master/LICENSE) nella repo.

### Contatti
[Telegram](https://t.me/michelepenzo)