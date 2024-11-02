#model/category.py

from datetime import datetime

from database.database import Database

class Category:
    def __init__(self, name, description=None):
        self._name = name
        self._description = description
        self._creation_date = datetime.now()
        self._last_update = datetime.now()

    def __repr__(self):
        return (f"Category(name={self._name}, description={self._description}, creation_date={self._creation_date}, "
                f"last_update={self._last_update})")

    def save(self):
        db = Database()
        db.execute_query("INSERT INTO categories (name, description) VALUES (?, ?)",
                         (self._name, self._description))
    
    def select_by_id(self, id):
        db = Database()
        data = db.fetch_data("SELECT * FROM categories WHERE id = ?", (id,))
        if data:
            return Category(data[0][1], data[0][2])
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
    def last_update(self):
        return self._last_update
    
    @last_update.setter
    def last_update(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Last update must be a datetime object")
        self._last_update = value