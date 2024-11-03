# /models/category.py

from datetime import datetime
from database.database import Database

class Category:
    def __init__(self, name, description=None, db=None):
        """
        Initializes a new category object

        :param name: str
        :param description: str
        :param db: Database
        """
        self.name = name.lower()
        self.description = description.lower()
        self._creation_date = datetime.now()
        self._last_update = datetime.now()
        self._db = db or Database()

    def __repr__(self):
        return (f"Category(name={self._name}, description={self._description}, "
                f"creation_date={self._creation_date}, last_update={self._last_update})")

    def save(self):
        """
        Saves the category to the database
        """
        self._db.execute_query(
            "INSERT INTO categories (name, description) VALUES (?, ?)",
            (self._name, self._description)
        )
    
    # Class methods

    @classmethod
    def select_all(cls, db=None):
        """
        Select all categories

        :param db: Database

        :returns: id, name, description
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM categories")
        
        categories = []
        for row in data:
            category = cls(row[1], row[2])
            category.id = row[0]
            categories.append(category)
        return categories

    
    @classmethod
    def select_by_id(cls, id, db=None):
        """
        Select a category by its id

        :param id: int
        :param db: Database

        :returns: name, description
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM categories WHERE id = ?", (id,))
        return cls(data[0][1], data[0][2]) if data else None
    
    @classmethod
    def select_by_name(cls, name, db=None):
        """
        Select a category by its name
        
        :param name: str
        :param db: Database
        :returns: id, name, description
        """
        db = db or Database() 
        data = db.fetch_data("SELECT * FROM categories WHERE name = ?", (name.lower(),))
        return cls(data[0][1], data[0][2]) if data else None
    
    # Decorators methods

    @staticmethod
    def _general_update_last_modified(func):
        """
        Decorator to update the last update date of the object
        """
        def general_update(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self._last_update = datetime.now()
            return result
        return general_update

    # Getters and setters

    @property
    def name(self):
        return self._name
    
    @name.setter
    @_general_update_last_modified
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        elif not isinstance(value, str):
            raise TypeError("Name must be a string")

        self._name = value
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    @_general_update_last_modified
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        elif not isinstance(value, str):
            raise TypeError("Description must be a string")
        
        self._description = value

    @property
    def last_update(self):
        return self._last_update
