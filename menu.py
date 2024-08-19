import schema
import sys

def prompt_menu(mydb):
    while True:
        x = input("Wipe Database: 1\n"
                  "Fill Database w/ Default Values: 2\n"
                  "Option: ").strip()

        match int(x):
            case 1:
                schema.reset_db(mydb)
            case 2:
                schema.fill_db_with_default_values(mydb)
            case _:
                mydb.close()
                sys.exit("Exiting database") # improve
