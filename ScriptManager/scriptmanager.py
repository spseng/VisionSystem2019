import time
import threading
from networktables import NetworkTables as nt

import tape3
import thread_example
import ball

ip = "10.31.51.43"

nt.initialize(server=ip)
table = nt.getTable("chooser_data")


stop_message = [0]

def start_tape():
    tape3.main(stop_message)

def start_ball():
    ball.main(stop_message)

def start_example():
    thread_example.main(stop_message)

def valueChanged(table, key, value, isNew):
    print("Value changed:", table, key, value)
    # 0 stops everything
    # 1 stops everything but tape detector
    # 2 stops everything but ball detector
    stop_message[0] = 0
    value = int(value)
    stop_message[0] = value
    
    if value != 0:
        time.sleep(1)
        
        print("[*]Starting thread: {}".format(value))
        t = threading.Thread(target=target_list[value])
        t.start()

def connectionListener(info, connected):
    print(info, "Connected:", connected)

target_list=[0, start_tape, start_ball, start_example]

nt.addConnectionListener(connectionListener)

table.addEntryListener(valueChanged)

while True:
    time.sleep(5)

