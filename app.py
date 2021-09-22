import logging
import sys


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
handler = logging.StreamHandler(sys.stdout)
logging.getLogger('').addHandler(handler)

if __name__ == "__main__":
    pass