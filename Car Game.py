command = ""
engine_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if engine_started:
            print("The car is already started! ")
        else:
            engine_started = True
            print("Car started...")
    elif command == "stop":
        if not engine_started:
            print("Car is already stopped! ")
        else:
            engine_started = False
            print("Car stopped...")
    elif command == "help":
        print("""
start - To start the car. 
stop - To stop the car.
quit - Quit the game.
        """)
    elif command == "quit":
        break
    else:
        print("Invalid input, try again. ")