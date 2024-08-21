from mysql.connector import Error
import schema_values

def reset_db(mydb):
    cursor = mydb.cursor()
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table_name, table_query in schema_values.tables.items():
            try:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                cursor.execute(table_query)
                #print(f"Table '{table_name}' created")
            except Error as err:
                print(f"{table_name} creation failed: {err}")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    except Error as err:
        print(f"Error occurred: {err}")

    cursor.close()

def fill_db_with_default_values(mydb):
    reset_db(mydb)
    cursor = mydb.cursor()
    for insert_name, insert_query in schema_values.inserts.items():
        try:
            cursor.execute(insert_query)
            print(f"Values for '{insert_name}' inserted")
        except Error as err:
            print(f"{insert_name} creation failed: {err}")

    cursor.close()