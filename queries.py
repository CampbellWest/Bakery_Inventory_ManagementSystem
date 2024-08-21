from mysql.connector import Error

def custom_select_query(mydb):

    query = input("Custom Query: ").strip()

    try:
        if query[:6].lower() == "select":
            cursor = mydb.cursor()
            cursor.execute(query)
            for x in cursor:
                print(x)
        else:
            print("Invalid SELECT Query")

    except Error as err:
        print(f"Error Occurred: {err}")


