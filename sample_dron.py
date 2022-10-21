from djitellopy import Tello
from threading import Thread
import time


tello = Tello()
def run_thread():
    while True:
        str_command = input(">> ")

        if str_command == "b":
            print(f"Battery: {tello.get_battery()}%")
        elif str_command == "exit":
            break


tello.connect()
time.sleep(2)
thread = Thread(target=run_thread)
thread.start()
