#imports
import menu
import database

def main():

    mydb = database.connect_to_my_db()
    mydb.autocommit = True #check this out

    menu.prompt_menu(mydb)

    mydb.close()

if __name__ == "__main__":
    main()