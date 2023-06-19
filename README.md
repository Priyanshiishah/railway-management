# RAILWAY MANAGEMENT SYSTEM
___

This is a Railway Management system in which a user can book tickets, cancel reservations, check fares etc. 
It uses MySQL as the backend database. 


## FOLDERS
___

1. Assets : Contains the data that is to be inserted in the MySQL tables in csv format
    - `Train_details.csv` : Contains all the data about the trains in the format (Train No, Station Code, Station Name, Arrival time, 
                           Departure Time, Distance, Source Station, Source Station Name, Destination Station, Destination Station Name)

2. core : Contains all the files that are required by the project to work
   - `__init__.py` : Makes the folder to be recognized as a module
   - `Checks.py` : This file contains the functions that verify the requirements of the Project
   - `InsertData.py` : This file contains the functions to insert the data in the MySQL tables
   - `User_Functions.py` : This file contains the function that allow a user to perform certain task
   - `Other.py` : This file contains some commonly used functions


## ROOT FOLDER FILES
___

- `Main.py` : This is the main file that connects all the other modules and is used to run the project

- `requirements.txt` : It contains the required packages for this project to work that can be installed via the command 
`pip3 install -r requirements.txt`


## FEATURES
___

1. Book a Ticket: Users can book a ticket
2. Cancel a Booking: Users can cancel a booked ticket
3. Check Fares: Users can check fares before booking
4. Show my Bookings: User can check their bookings
5. Show Available Trains: Users can see the available trains 
6. Clear Screen: Clears the terminal screen
7. Menu: Shows the menu
8. About: Prints the content of this file to the screen
9. Exit: Exit the program


## ENVIRONMENT SETUP
___

1. Clone the Repository to your machine.
2. Create a Virtual Environment using virtualenv or pipenv.
3. `pip3 install -r Requirements.txt` to install the required packages automatically.
4. Make sure the MySQL Service is running and add environment variables as DB_USERNAME and DB_PASSWORD `.env` file.
5. `python3 Main.py` to see if the program is running correctly and is able to connect to MySQL Server.