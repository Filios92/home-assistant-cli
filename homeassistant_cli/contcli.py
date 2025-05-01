import re
import sys
import shlex
from homeassistant_cli.cli import run as run2

def run():
  while True:
    try:
      line = input('>')
      if len(line) == 0:
        continue
      print(line)
      sys.argv = [sys.argv[0]] + shlex.split(line)
      print(sys.argv)
      run2()
    except KeyboardInterrupt:
      return
    except Exception as e:
      print(e)
        