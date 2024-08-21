tables = {
    "ingredients": """
        CREATE TABLE `ingredients`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL
        );""",

    "categories": """          
        CREATE TABLE `categories`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL
        );""",

    "recipes": """
        CREATE TABLE `recipes`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `instructions` TEXT NOT NULL,
            `baking_time` INT NOT NULL COMMENT 'in minutes',
            `baking_temp` INT NOT NULL COMMENT 'in fahrenheit'
        );""",

    "products": """
        CREATE TABLE `products` (
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL,
            `category_id` INT UNSIGNED NOT NULL,
            `price` DECIMAL(3, 2) NOT NULL,
            `recipe_id` INT,
            FOREIGN KEY(`category_id`) REFERENCES `categories`(`id`),
            FOREIGN KEY(`recipe_id`) REFERENCES `recipes`(`id`)
        );""",

    "product_ingredient": """
        CREATE TABLE `product_ingredient`(
            `product_id` INT UNSIGNED NOT NULL,
            `ingredient_id` INT UNSIGNED NOT NULL,
            `quantity_in_kg` DECIMAL(5, 3) NOT NULL,
            FOREIGN KEY(`product_id`) REFERENCES `products`(`id`),
            FOREIGN KEY(`ingredient_id`) REFERENCES `ingredients`(`id`)
        );""",

    "sales": """
        CREATE TABLE `sales`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `date` DATE NOT NULL,
            `total_amount` DECIMAL(4, 2) NOT NULL
        );""",

    "sales_details": """
        CREATE TABLE `sales_details`(
            `sale_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `product_id` INT UNSIGNED NOT NULL,
            `quantity_sold` INT NOT NULL,
            `sale_price` DECIMAL(8, 2) NOT NULL,
            FOREIGN KEY(`sale_id`) REFERENCES `sales`(`id`),
            FOREIGN KEY(`product_id`) REFERENCES `products`(`id`)
        );""",

    "suppliers": """
        CREATE TABLE `suppliers`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` TEXT NOT NULL,
            `contact_email` TEXT NOT NULL,
            `contact_phone` TEXT NOT NULL,
            `address` TEXT NOT NULL
        );""",

    "orders": """
        CREATE TABLE `orders`(
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `supplier_id` INT UNSIGNED NOT NULL,
            `order_date` DATE NOT NULL,
            `status` ENUM('ordered', 'shipped', 'received'),
            FOREIGN KEY(`supplier_id`) REFERENCES `suppliers`(`id`)
        );""",

    "order_details": """
        CREATE TABLE `order_details`(
            `order_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
            `ingredient_id` INT UNSIGNED NOT NULL,
            FOREIGN KEY(`order_id`) REFERENCES `orders`(`id`),
            FOREIGN KEY(`ingredient_id`) REFERENCES `ingredients`(`id`)
        );"""
    }

inserts = {
    "ingredients":
        """
        INSERT INTO ingredients (name)
        VALUES 
            ("flour"),
            ("ww flour"),
            ("water"),
            ("yeast"),
            ("salt"),
            ("sugar"),
            ("oil"),
            ("milk"),
            ("egg"),
            ("improver"),
            ("gluten"),
            ("levain"),
            ("malt"),
            ("cheese"),
            ("dried fruit"),
            ("scone mix"),
            ("cinnamon");
        """,

    "categories":
        """
        INSERT INTO categories (name)
        VALUES 
            ("sandwich bread"),
            ("artisan"),
            ("sweet"),
            ("rolls"),
            ("croissants"),
            ("danish"),
            ("tarts");
        """,

    "recipes":
        """
        INSERT INTO recipes (instructions, baking_time, baking_temp)
        VALUES 
            ('3 cuts diagonal cuts', 60, 450),
            ('Add toppings', 90, 425),
            ('1 cut down middle', 720, 450),
            ('3 parallel cuts', 90, 375),
            ('Prepare dough, shape into rolls', 60, 375),
            ('Prepare dough, shape into buns', 60, 375),
            ('Prepare dough, shape into buns', 60, 375),
            ('Egg wash then add toppings', 90, 375),
            ('Egg wash', 30, 375),
            ('Egg wash', 30, 375),
            ('Egg wash', 30, 375),
            ('Egg wash', 30, 375),
            ('Prepare dough, shape into rolls', 60, 375),
            ('Egg wash then add toppings', 90, 375),
            ('Egg wash then add toppings', 90, 375),
            ('Egg wash then add toppings', 90, 375),
            ('Defrost', 60, 350),
            ('Defrost', 60, 350),
            ('Prepare dough, shape into scones', 30, 375),
            ('Prepare dough, add fruit, shape into scones', 30, 375),
            ('Prepare dough, add cheese, shape into scones', 30, 375),
            ('Prepare dough, shape into loaf', 60, 375),
            ('Prepare dough, shape into loaf', 60, 375);
        """,

    "product_ingredient":
        """
        INSERT INTO product_ingredient (product_id, ingredient_id, quantity_in_kg)
        VALUES 
            (1, 1, 1.000), 
            (1, 3, 0.700), 
            (1, 4, 0.010), 
            (1, 5, 0.015),
        
            (2, 1, 1.200), 
            (2, 3, 0.800), 
            (2, 4, 0.015), 
            (2, 5, 0.020), 
            (2, 7, 0.050),
        
            (3, 1, 1.500), 
            (3, 3, 1.000), 
            (3, 4, 0.015), 
            (3, 5, 0.015), 
            (3, 12, 0.200),
        
            (4, 1, 1.200), 
            (4, 3, 0.800), 
            (4, 4, 0.015), 
            (4, 5, 0.015), 
            (4, 12, 0.150),
        
            (5, 1, 1.000), 
            (5, 3, 0.600), 
            (5, 4, 0.020), 
            (5, 5, 0.020), 
            (5, 10, 0.020),
        
            (6, 1, 1.000), 
            (6, 3, 0.600), 
            (6, 4, 0.020), 
            (6, 5, 0.020), 
            (6, 10, 0.020),
        
            (7, 1, 1.000), 
            (7, 3, 0.600), 
            (7, 4, 0.020), 
            (7, 5, 0.020),
            (7, 10, 0.020),
        
            (8, 1, 1.200), 
            (8, 3, 0.800), 
            (8, 4, 0.020), 
            (8, 5, 0.015), 
            (8, 13, 0.010), 
            (8, 10, 0.020),
        
            (9, 1, 1.000), 
            (9, 18, 0.100), 
            (9, 6, 0.050), 
            (9, 8, 0.020), 
            (9, 9, 0.020), 
            (9, 4, 0.020), 
            (9, 5, 0.015), 
            (9, 10, 0.020),
        
            (10, 1, 1.000), 
            (10, 18, 0.100), 
            (10, 8, 0.020), 
            (10, 9, 0.020), 
            (10, 4, 0.020), 
            (10, 5, 0.015),
        
            (11, 1, 1.000), 
            (11, 18, 0.100), 
            (11, 8, 0.020), 
            (11, 9, 0.020), 
            (11, 4, 0.020), 
            (11, 5, 0.015),
        
            (12, 1, 1.000), 
            (12, 18, 0.100), 
            (12, 6, 0.050), 
            (12, 8, 0.020), 
            (12, 9, 0.020), 
            (12, 4, 0.020), 
            (12, 5, 0.015),
        
            (13, 1, 1.000), 
            (13, 18, 0.100), 
            (13, 6, 0.050),
            (13, 10, 0.020), 
            (13, 4, 0.020), 
            (13, 5, 0.015), 
            (13, 17, 0.020),
        
            (14, 1, 1.000), 
            (14, 18, 0.100), 
            (14, 6, 0.050), 
            (14, 8, 0.020), 
            (14, 9, 0.020), 
            (14, 4, 0.020), 
            (14, 5, 0.015), 
            (14, 14, 0.050),
        
            (15, 1, 1.000), 
            (15, 18, 0.100), 
            (15, 6, 0.050), 
            (15, 8, 0.020), 
            (15, 9, 0.020), 
            (15, 4, 0.020), 
            (15, 5, 0.015),
        
            (16, 1, 1.000), 
            (16, 18, 0.100), 
            (16, 6, 0.050), 
            (16, 8, 0.020), 
            (16, 9, 0.020), 
            (16, 4, 0.020), 
            (16, 5, 0.015),
        
            (17, 15, 0.050), 
            (17, 19, 0.100),
        
            (18, 6, 0.100), 
            (18, 18, 0.050), 
            (18, 19, 0.100),
        
            (19, 3, 0.050), 
            (19, 16, 0.100),
        
            (20, 3, 0.050), 
            (20, 16, 0.100), 
            (20, 15, 0.050),
        
            (21, 3, 0.050), 
            (21, 16, 0.100), 
            (21, 14, 0.050),
        
            (22, 1, 1.000), 
            (22, 3, 0.600), 
            (22, 4, 0.020), 
            (22, 5, 0.015),
            (22, 10, 0.010),
        
            (23, 2, 1.000), 
            (23, 3, 0.600), 
            (23, 4, 0.020), 
            (23, 5, 0.015),
            (23, 10, 0.010);
        """,

    "suppliers":
        """
        INSERT INTO suppliers (name, contact_email, contact_phone, address)
        VALUES 
            ("Baker's Best Supplies", "info@bakersbest.com", "905-123-4567", "123 Main St, Toronto, ON M5A 1A1"),
            ("Flour Power Inc.", "contact@flourpower.com", "905-234-5678", "456 Elm St, Mississauga, ON L5G 1K7"),
            ("Yeast & Co.", "support@yeastco.com", "905-345-6789", "789 Oak St, Hamilton, ON L8P 2Y5"),
            ("Sweet Ingredients Ltd.", "hello@sweetingredients.com", "905-456-7890", "321 Maple Ave, Burlington, ON L7T 1H7"),
            ("The Bread Basket", "sales@breadbasket.com", "905-567-8901", "654 Pine Rd, London, ON N5V 3A1");
        """
}