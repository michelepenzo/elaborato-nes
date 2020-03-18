# Sistemi Embedded di Rete

Esmpio di NCS, svolto come progetto per il corso NES. <br>

## Prerequisiti

- Server: SO Linux (sviluppato e testato su Ubuntu 19.10) <br>
- Client: Smartphone Android <br>
- Dispositivi connessi alla stessa rete WiFi. <br>

## Funzionamento
1. Eseguire il file per installare i pacchetti necessari:
```
./setup.sh
```


2. Eseguire il __server__ guardando i valori dell'indirizzo IP e della porta.
```
python3 NCSserver/server.py
```

3. Per il __client__ installare il file ``NCS-client.apk``, aprirlo e inserire i valori ottenuti dal server.


## Licenza
Consultare il file [LICENSE](https://github.com/michelepenzo/nes/blob/master/LICENSE) nella repo.

### Contatti
[Telegram](https://t.me/michelepenzo)