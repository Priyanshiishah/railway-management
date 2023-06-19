# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules
import os

from mysql.connector import connect
from mysql.connector.errors import ProgrammingError, Error

import core.InsertData as Insert


# Functions


def check_database():
    """
    check_database() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = connect(host="localhost", user=os.getenv('DB_USERNAME'),
                 database="", password=os.getenv('DB_PASSWORD'))
    cur = db.cursor()
    result = None

    try:
        cur.execute("use railway;")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True

    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database railway;")
        cur.execute("use railway;")
        create_tables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def create_tables():
    """
    create_tables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = connect(host="localhost", user=os.getenv('DB_USERNAME'),
                 database="railway", password=os.getenv('DB_PASSWORD'))
    cur = db.cursor()

    cur.execute(
        "create table train_info (Train_No varchar(10) NOT NULL, Station_Code varchar(20) NOT NULL, "
        "Station_Name varchar(30) NOT NULL, Arrival_Time varchar(20) NOT NULL, Departure_Time varchar(20) NOT NULL, "
        "Distance varchar(10) NOT NULL, Source_Station_Code varchar(20) NOT NULL, "
        "Source_Station_Name varchar(70) NOT NULL, Destination_Station_Code varchar(20) NOT NULL, "
        "Destination_Station_Name varchar(60) NOT NULL);")

    cur.execute(
        "create table bookings (Train_No int NOT NULL, Passenger_Name varchar(30) NOT NULL, "
        "Mobile_No varchar(10) NOT NULL, Passenger_Aadhaar varchar(12) NOT NULL, "
        "Date_Of_Booking varchar(20) NOT NULL, Booking_ID int NOT NULL, Class varchar(20) NOT NULL);")

    Insert.insert_train_data()

    cur.close()
    db.close()


def check_connection():
    """
    check_connection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = connect(host='localhost',
                             database='',
                             user=os.getenv('DB_USERNAME'),
                             password=os.getenv('DB_PASSWORD'))
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True
