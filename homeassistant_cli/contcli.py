import re
import sys
from homeassistant_cli.cli import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    #sys.exit(run())
    while True:
      try:
        line = input('>')
        if len(line) == 0:
          continue
        print(line)
        sys.argv = [sys.argv[0]] + line.split(' ')
        print(sys.argv)
        run()
      except KeyboardInterrupt:
        sys.exit()
        