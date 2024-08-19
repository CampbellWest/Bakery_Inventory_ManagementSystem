#imports
import schema

def main():
    mydb = schema.connect_to_my_db()
    mydb.autocommit = True #check on this

    x = input("""Wipe Database: 1 \nFill Database w/ Default Values: 2 \nOption: """)

    match int(x):
        case 1:
            schema.reset_db(mydb)
        case 2:
            schema.fill_db_with_default_values(mydb)

        # case delete
        # case add/insert
        # case export to csv

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ingredients")
    for x in cursor:
        print(x)

    cursor.close()
    mydb.close()

if __name__ == "__main__":
    main()