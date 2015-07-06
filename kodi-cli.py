#!/usr/bin/env python

# See: http://www.tuxradar.com/content/code-project-build-ncurses-ui-python
from os import system
import curses
import requests
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r'config.ini'))
base_url= config.get('Kodi', 'server')
port = config.get('Kodi', 'port')
url = "http://{}:{}/jsonrpc".format(base_url,port)

headers = {'content-type': 'application/json'}



def send_input_command(cmd):
  payload = json.dumps({"jsonrpc": "2.0", 
                        "method": cmd})
  return requests.request("POST", url, data=payload, headers=headers)


def send_player_command(cmd, **kwargs):
  payload = json.dumps({"jsonrpc": "2.0", 
                        "method": cmd,
                        "id": 1,
                        "params": kwargs})
  return requests.request("POST", url, data=payload, headers=headers)



send_input_command("Input.Down")

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input


x = 0

while x != ord('q'):
     screen = curses.initscr()
     curses.echo()  
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, "Move... (Arrow keys also work for navigation)")
     screen.addstr(4, 4, "w: Up")
     screen.addstr(5, 4, "a: Left")
     screen.addstr(6, 4, "s: Down")
     screen.addstr(7, 4, "d: Right")
     screen.addstr(8, 4, "g: Select")
     screen.addstr(9, 4, "b: Back")
     screen.addstr(10, 4, "h: Home")
     screen.addstr(2, 54, "------------ Media Controls ---------- ")
     screen.addstr(4, 54, "p: Play/Pause")
     screen.addstr(5, 54, "f: Full Screen")
     screen.addstr(6, 54, "X: Stop")

     screen.addstr(12, 4, "q: Exit")

     screen.refresh()
     
     x = screen.getch()
     screen.addstr(12, 5, str(x))

     if x == ord('w') or x == 65:
      send_input_command("Input.Up")


     if x == ord('a') or x == 68:
      send_input_command("Input.Left")
 
     if x == ord('s') or x == 66:
      send_input_command("Input.Down")

     if x == ord('d') or x == 67:
       send_input_command("Input.Right")

     if x == ord('g'):
       send_input_command("Input.Select")
     
     if x == ord('h'):
       send_input_command("Input.Home")

     if x == ord('b'):
       send_input_command("Input.Back")


     if x == ord('b'):
       send_input_command("Input.Back")
     if x == ord('p'):
       send_player_command("Player.PlayPause", playerid=0)

     if x == ord('f'):
       send_player_command("GUI.SetFullscreen", fullscreen=True)

     if x == ord('X'):
       send_player_command("Player.Stop", playerid=0)
curses.endwin()
