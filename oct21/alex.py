from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get.battery)