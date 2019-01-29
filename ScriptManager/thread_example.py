import time

def main(stop_message):

    while True:
        x = stop_message.get()
        
        print("[*]Thread 3 queue:" , x)
        
        if x != 3:
            print("[*]Thread 3 exiting")
            return
        
        time.sleep(1)

