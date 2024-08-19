import mysql.connector
from mysql.connector import Error

def main():
    return


def connect_to_my_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123",
        database="bakery_inventory"
    )

def reset_db(mydb):
    tables = {
    "ingredients": """
        CREATE TABLE `ingredients`(
            `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL
        );""",
    "categories": """          
        CREATE TABLE `categories`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL
        );""",
    "recipes": """
        CREATE TABLE `recipes`(
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `instructions` TEXT NOT NULL,
            `baking_time` INT NOT NULL COMMENT 'in minutes',
            `baking_temp` INT NOT NULL COMMENT 'in fahrenheit',
            `servings` INT NOT NULL
        );""",
    "products": """
        CREATE TABLE `products` (
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL,
            `category_id` INT NOT NULL,
            `price` DECIMAL(3, 2) NOT NULL,
            `description` TEXT NULL,
            `recipe_id` INT,
            FOREIGN KEY(`recipe_id`) REFERENCES `recipes`(`id`)
        );""",
    "product_ingredient": """
        CREATE TABLE `product_ingredient`(
            `product_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
            `ingredient_id` INT NOT NULL,
            `quantity_in_kg` DECIMAL(3, 3) NOT NULL,
            FOREIGN KEY(`product_id`) REFERENCES `products`(`id`),
            FOREIGN KEY(`ingredient_id`) REFERENCES ingredients(id)
        );"""
    }

    cursor = mydb.cursor()
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table_name, table_query in tables.items():
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
    insert_ingredients = """
    INSERT INTO bakery_inventory.ingredients (name)
    VALUES ("flour"),
    ("yeast"),
    ("water")
    """

    cursor = mydb.cursor()
    cursor.execute(insert_ingredients)
    #mydb.commit()

if "__name__" == "__main__":
    main()








