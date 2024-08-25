import schema
import queries
import sys
import database

import pandas as pd
from sqlalchemy import create_engine

def prompt_menu(mydb):
    while True:
        x = input("\nProducts: 1\n"
                  "Orders: 2\n"
                  "Sales: 3\n"
                  "Custom SELECT Query: 4\n"
                  "Advanced Menu: 5\n"
                  "Exit: 6\n"
                  "Option: ").strip()

        match int(x):
            case 1:
                return
                #product related data
            case 2:
                return
                #order related data
            case 3:
                return
                #sales related data
            case 4:
                queries.custom_select_query(mydb)
            case 5:
                advanced_menu(mydb)
            case _:
                mydb.close()
                sys.exit("Exiting database") # improve


def advanced_menu(mydb):
    print("\nRe-Enter Password")
    if database.connect_to_my_db():
        while True:
            x = input("\nWipe Database: 1\n"
                      "Reset with Default Values: 2\n"
                      "Export to CSV: 3\n"
                      "Option: ").strip()
            match int(x):
                case 1:
                    schema.reset_db(mydb)
                case 2:
                    schema.fill_db_with_default_values(mydb)
                case 3:
                    export_to_csv()
                case _:
                    return


def export_to_csv():

    username = "root"
    password = "Password123"
    host = "localhost"
    database = "bakery_inventory"

    #give options on what to export from

    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

    query = "SELECT * FROM products"
    df = pd.read_sql(query, engine)

    df.to_csv("Output.csv", index=False)

