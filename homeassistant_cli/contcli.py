import re
import sys
from homeassistant_cli.cli import run as run2

def run():
  while True:
    try:
      line = input('>')
      if len(line) == 0:
        continue
      print(line)
      sys.argv = [sys.argv[0]] + line.split(' ')
      print(sys.argv)
      run2()
    except KeyboardInterrupt:
      return
        