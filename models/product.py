# model/product.py

from datetime import datetime

from database.database import Database
from utils.barCode import BarCode



class Product:
    def __init__(self, name, category_id, manufacturer_id, price, quantity, description=None):
        self._name = name
        self._description = description
        self._category_id = category_id
        self._manufacturer_id = manufacturer_id
        self._price = price
        self._quantity = quantity
        self._code = BarCode.generate_barcode("038", "001")
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

    # Select a product by ID
    @classmethod
    def select_by_id(cls, id):
        db = Database()
        data = db.fetch_data("SELECT * FROM products WHERE id = ?", (id,))
        if data:
            return Product(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6])
        else:
            return None
        
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
        if not isinstance(self._description, str):
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

