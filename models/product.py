# model/product.py

from datetime import datetime

from database.database import Database
from utils.barCode import BarCode
from utils.type import Type

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
    def select_product_by_price(cls, price, db = None):
        """
        search for products by price
        :param
            price: str
            db: Database    
        :returns: list
        """
        if not Type.is_float(price):
            raise ValueError("Price must be number or decimal")
        
        db = db or Database()
        data = db.fetch_data(
            """
            SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
           p.price, p.quantity, p.code
           FROM products p
           JOIN categories c ON p.category_id = c.id
           JOIN manufacturer m ON p.manufacturer_id = m.id
           WHERE p.price = ?
           """, (price,))
        
        return data if data else ()
    
    @classmethod
    def select_product_by_quantity(cls, quantity, db = None):
        """
        search for products by quantity
        :param
            quantity: str
            db: Database    
        :returns: list
        """
        if not Type.is_int(quantity):
            raise ValueError("Quantity must be number")
        
        db = db or Database()
        data = db.fetch_data(
            """
            SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
           p.price, p.quantity, p.code
           FROM products p
           JOIN categories c ON p.category_id = c.id
           JOIN manufacturer m ON p.manufacturer_id = m.id
           WHERE p.quantity = ?
           """, (quantity,))
        
        return data if data else ()
    
    @classmethod
    def select_product_by_category(cls, category, db = None):
        """
        search for products by category
        :param
            category: str
            db: Database    
        :returns: list
        """
        
        db = db or Database()
        data = db.fetch_data(
            """
            SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
           p.price, p.quantity, p.code
           FROM products p
           JOIN categories c ON p.category_id = c.id
           JOIN manufacturer m ON p.manufacturer_id = m.id
           WHERE LOWER(c.name) LIKE ?
           """, (f"{category.lower()}%",))
        
        return data if data else ()
    
    @classmethod
    def select_product_by_company(cls, company, db = None):
        """
        search for products by company
        :param
            company: str
            db: Database    
        :returns: list
        """
        
        db = db or Database()
        data = db.fetch_data(
            """
            SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
           p.price, p.quantity, p.code
           FROM products p
           JOIN categories c ON p.category_id = c.id
           JOIN manufacturer m ON p.manufacturer_id = m.id
           WHERE LOWER(m.name) LIKE ?
           """, (f"{company.lower()}%",))
        
        return data if data else ()
    
    @classmethod
    def select_product_by_creation_date(cls, date, db=None):
        """
        Select for products by creation date
        :param 
            date: str
            db: Database

        :returns: id, name, description, category_name, manufacturer_name, price, quantity, code
        """
        if not Type.is_date(date):
            raise ValueError("Date must be in the format YYYY-MM-DD")
        db = db or Database()
        data = db.fetch_data("SELECT * FROM products WHERE date(creation_date) = date(?)", (date,))
        return data if data else ()
    
    @classmethod
    def select_product_by_last_update(cls, date, db=None):
        """
        Select for products by last update date
        :param 
            date: str
            db: Database

        :returns: id, name, description, category_name, manufacturer_name, price, quantity, code
        """
        if not Type.is_date(date):
            raise ValueError("Date must be in the format YYYY-MM-DD")
        
        db = db or Database()
        data = db.fetch_data("SELECT * FROM products WHERE date(last_update) = date(?)", (date,))
        return data if data else ()
    
    @classmethod
    def select_all(cls, db=None):
        """
        Select all products along with their category and manufacturer names
        :param db: Database
        :returns: list of tuples containing (id, name, description, category_name, manufacturer_name, price, quantity, code)
        """
        db = db or Database()
        # Update the query to join with categories and manufacturers
        query = """
        SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
        p.price, p.quantity, p.code
        FROM products p
        JOIN categories c ON p.category_id = c.id
        JOIN manufacturer m ON p.manufacturer_id = m.id
        """

        data = db.fetch_data(query)
        
        products = []
        for row in data:
            product_info = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'category_name': row[3],
                'manufacturer_name': row[4],
                'price': row[5],
                'quantity': row[6],
                'code': row[7],
                }
            products.append(product_info)
        return products
    
    @classmethod
    def select_product_by_partial_name(cls, name, db=None):
        """
        Select for products by partial name
        :param
            name: str
            db: Database    
        :returns: list
        """
        db = db or Database()
        data = db.fetch_data(
            """
            SELECT p.id, p.name, p.description, c.name AS category_name, m.name AS manufacturer_name, 
            p.price, p.quantity, p.code
            FROM products p
            JOIN categories c ON p.category_id = c.id
            JOIN manufacturer m ON p.manufacturer_id = m.id
            WHERE LOWER(p.name) LIKE ?
            """, (f"{name.lower()}%",))
        
        return data if data else ()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        elif not isinstance(value, str):
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
        if not value:
            raise ValueError("Price cannot be empty")
        elif not isinstance(value, float):
            raise TypeError("Price must be a float")
        elif value <= 0:
            raise ValueError("Price must be greater than 0")
        
        self._price = value
        self._last_update = datetime.now()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not value:
            raise ValueError("Quantity cannot be empty")
        elif not isinstance(value, int):
            raise TypeError("Quantity must be an integer")
        elif value < 0:
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

