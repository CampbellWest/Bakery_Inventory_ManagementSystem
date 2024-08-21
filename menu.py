import schema
import queries
import sys
import database

def prompt_menu(mydb):
    while True:
        x = input("\nCustom SQL SELECT Query: 1\n"
                  "Advanced Menu: 2\n"
                  "Option: ").strip()

        match int(x):
            case 1:
                queries.custom_select_query(mydb)
            case 2:
                advanced_menu(mydb)
            case _:
                mydb.close()
                sys.exit("Exiting database") # improve

def advanced_menu(mydb):
    print("\nRe-Enter Password")
    relog = database.connect_to_my_db()
    while True:
        x = input("\nWipe Database: 1\n"
                  "Reset with Default Values: 2\n"
                  "Option: ").strip()
        match int(x):
            case 1:
                schema.reset_db(mydb)
            case 2:
                schema.fill_db_with_default_values(mydb)
            case _:
                return