import time
import sys

def main(stop_message):

    while True:

        x = stop_message[0]

        
        print("[*]Thread 3 queue:" , x)
        
        if x != 3:
            print("[*]Thread 3 exiting")
            sys.exit()
        
        time.sleep(1)

