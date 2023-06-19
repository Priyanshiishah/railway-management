# This is the Main File that loads all the Other Modules
# Importing Required Modules

from time import sleep

from dotenv import load_dotenv

import core.Checks as Check
import core.Other as Other
import core.User_Functions as User

# Initial Checks
load_dotenv()

# Checking the Connection to the MySQL Server
connection_status = Check.check_connection()
if connection_status is False:
    quit()
else:
    Check.check_database()  # Checking for the Requirements of the Project

Other.clear_screen()  # Clear the Terminal Window

# Ask for the Input and Process it
Other.menu()

while True:
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.book_train()
    elif ans == "2":
        User.cancel_booking()
    elif ans == "3":
        User.check_fare()
    elif ans == "4":
        User.show_bookings()
    elif ans == "5":
        User.available_trains()
    elif ans == "6":
        Other.clear_screen()
        Other.menu()
    elif ans == "7":
        Other.menu()
    elif ans == "8":
        Other.clear_screen()
        Other.about()
        while True:
            ask = input("Do you want to Display Menu(Y/N): ")
            if ask in ["Y", "y"]:
                Other.menu()
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yes) or N (No)!")
    elif ans == "9":
        print("Closing all Connections..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
