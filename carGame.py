user_input = input("Enter 'help' to see the instructions: ")

if user_input.lower() == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")

directions = input('Enter a command: ')
while True:
    if directions.lower() == "start":
        print("Car started...Ready to go!")
    elif directions.lower() == "stop":
        print("Car stopped.")
    elif directions.lower() == "quit":
        break
    else:
        print("I don't understand that")
    directions = input('Enter a command: ')