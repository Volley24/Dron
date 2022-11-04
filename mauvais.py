from djitellopy import Tello

tello = Tello()

tello.connect()

print(f"Battery life: {tello.get_battery()}%")

def run_thread():
    while True:
        str_command = input(">> ")

        if str_command == "b":
            print(f"Battery: {tello.get_battery()}%")
        elif str_command == "exit":
            break

def main():
    tello.takeoff()
    nion = 40

    tello.move_up(50)
    tello.move_forward(nion)
    tello.move_back(nion * 2)
    tello.move_forward(nion)

    tello.move_left(nion)
    tello.move_right(nion * 2)
    tello.move_left(nion)

    tello.flip_back()

    tello.land()


if tello.get_battery() < 10:
    print("Your battery is LOW. Please insert another battery!!!")
else:
    main()
