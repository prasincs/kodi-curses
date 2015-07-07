# Kodi CLI 

For navigating from commandline. This is a very simple application written so I didn't have to reach to a remote control while watching tv. Might add a few things as needed.

You'll have to install the JSON-RPC service from settings in Kodi.


# How to Run

## Change the config to suit your setup

Save the following with appropriate changes as `config.ini`. 

```
[Kodi]
server=192.168.1.60
port=8080
```

## Install requirements

Only "requests" library is used other than curses. In case I'll add more things, follow the instructions.

`pip install -r requirements.txt `

## Run the application

`python kodi-cli.py`

### ???

### Profit
