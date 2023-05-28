import requests
import signal
import sys
import time
from pwn import *

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
def makeSQLI():

     



if __name__ == '__main__':
     
     time.sleep(10)
     makeSQLI()
