# Include the main set of functions that allow us to fly the drone
from djitellopy import Tello
from time import sleep

# Instantiate a new instance of the drone and connect to it
tello = Tello()
tello.connect()
print(tello.get_battery())

# ==============================================================================
# Simple movement demo #1
# -----------------------
#
#  In this example we use the simplified movement functions:
#    rotate_clockwise(numDegrees) / rotate_counter_clockwise(numDegrees)
#    move_up(numCm) / move_down(numCm)
#    move_left(numCm) / move_right(numCm)
#    move_forward(numCm) / move_back(numCm)
# ==============================================================================

# Cause drone to takeoff and hover
tello.takeoff()

# Exercise the various simple movement commands
tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)
tello.move_up(30)
tello.move_down(30)
tello.move_forward(30)
tello.move_back(30)
tello.move_left(30)
tello.move_right(30)

# Cause drone to land (hopefully you're somewhere safe!)
tello.land()
