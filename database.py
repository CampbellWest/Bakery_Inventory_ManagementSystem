import sys
import mysql.connector
from mysql.connector import Error

def connect_to_my_db():
    guesses = 0
    while True:
        x = input("Password: ").strip()
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password=x,
                database="bakery_inventory"
            )
            if db.is_connected():
                print("Connected to database\n")
                return db
        except Error as err:
            if guesses == 2:
                sys.exit("Too many incorrect guesses")
            print(f"Error: {err}")
            guesses += 1
            continue