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

inserts = {
    "ingredients":
        """
        INSERT INTO ingredients (name)
        VALUES ("flour"), 
               ("water"),
               ("yeast");
        """,
    "categories":
        """
        INSERT INTO categories (name)
        VALUES ("sourdough"),
               ("rye"),
               ("white");
        """
}