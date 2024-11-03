# model/product.py

from datetime import datetime

from database.database import Database
from utils.barCode import BarCode

class Product:
    def __init__(self, name, category_id, manufacturer_id, price, quantity, description= ""):
        self.name = name
        self.description = description
        self.category_id = category_id
        self.manufacturer_id = manufacturer_id
        self.price = price
        self.quantity = quantity
        self.code = BarCode.generate_barcode("038", "001")
        self._creation_date = datetime.now()
        self._last_update = datetime.now()

    def __repr__(self):
        return (f"Product(name={self._name}, category_id={self._category_id}, manufacturer_id={self._manufacturer_id}, "
                f"price={self._price}, quantity={self._quantity}, code={self._code}, description={self._description}, "
                f"creation_date={self._creation_date}, last_update={self._last_update})")
    
    def save(self):
        db = Database()
        db.execute_query("INSERT INTO products (name, description, category_id, manufacturer_id, price, quantity, code) "
                         "VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (self._name, self._description, self._category_id, self._manufacturer_id, self._price, self._quantity, self._code))

    @classmethod
    def select_by_id(cls, id):
        """
        Select a product by its id
        :param id: int
        :returns: name, description, category_id, manufacturer_id, price, quantity, code
        """
        db = Database()
        data = db.fetch_data("SELECT * FROM products WHERE id = ?", (id,))
        if data:
            return Product(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6])
        else:
            return None
    
    @classmethod
    def select_by_name(cls, name, db=None):
        """
        Select a product by its name
        :param
            name: str
            db: Database
        :returns: id, name, description, category_id, manufacturer_id, price, quantity, code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM products WHERE name = ?", (name.lower(),))
        return cls(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6]) if data else None
    
    @classmethod
    def select_all(cls, db=None):
        """
        Select all products
        :param db: Database
        :returns: id, name, description, category_id, manufacturer_id, price, quantity, code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM products")

        products = []
        for row in data:
            product = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            product.id = row[0]
            products.append(product)
        return products
    
    @classmethod
    def select_all_for_display(cls, db=None):
        """
        Select all products with category and manufacturer names for display purposes.
        :param db: Database
        :returns: List of products with category and manufacturer names
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM products")
        
        products_for_display = []
        for row in data:
            category = Category.select_by_id(row[2])  
            manufacturer = Company.select_by_id(row[3]) 
            
            product_display = {
                'id': row[0],
                'name': row[1],
                'description': row[7],
                'category_name': category.name if category else None,
                'manufacturer_name': manufacturer.name if manufacturer else None,
                'price': row[4],
                'quantity': row[5],
                'code': row[6]
                }
            products_for_display.append(product_display)
        return products_for_display


        
    # Getters and setters for the attributes

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
        self._last_update = datetime.now()
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        self._description = value
        self._last_update = datetime.now()

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Category ID must be an integer")
        if value < 0:
            raise ValueError("Category ID must be greater than or equal to 0")
        self._category_id = value
        self._last_update = datetime.now()

    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Manufacturer ID must be an integer")
        if value < 0:
            raise ValueError("Manufacturer ID must be greater than or equal to 0")
        self._manufacturer_id = value
        self._last_update = datetime.now()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = value
        self._last_update = datetime.now()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("Quantity must be an integer")
        if value < 0:
            raise ValueError("Quantity must be greater than or equal to 0")
        self._quantity = value
        self._last_update = datetime.now()

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not isinstance(value, str):
            raise TypeError("Code must be a string")
        if len(value) != 12:
            raise ValueError("Code must be 12 characters long")
        self._code = value
        self._last_update = datetime.now()

    @property
    def last_update(self):
        return self._last_update
    
    @last_update.setter
    def last_update(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Last update must be a datetime object")
        self._last_update = value

