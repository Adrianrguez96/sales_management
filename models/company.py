# /models/company.py

from datetime import datetime
from database.database import Database

class Company:
    def __init__(self, name, description=None, factory_code=None, db=None):
        """
        Initializes a new manufacturer object
        :param name: str
        :param description: str
        :param factory_code: int
        :param db: Database
        """
        self.name = name.lower()
        self.description = description.lower()
        self.factory_code = factory_code
        self._creation_date = datetime.now()
        self._last_update = datetime.now()
        self._db = db or Database()

    def __repr__(self):
        return (f"Manufacturer(name={self._name}, description={self._description}, "
                f"factory_code={self._factory_code}, creation_date={self._creation_date}, last_update={self._last_update})")
    
    def save(self):
        """
        Saves the manufacturer to the database
        """
        self._db.execute_query(
            "INSERT INTO manufacturer (name, description, factory_code) VALUES (?, ?, ?)",
            (self._name, self._description, self._factory_code)
        )

    # Class methods

    @classmethod
    def select_all(cls, db=None):
        """
        Select all manufacturers
        :param db: Database
        :returns: id, name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer")
        
        manufacturers = []
        for row in data:
            manufacturer = cls(row[1], row[2], row[3])
            manufacturer.id = row[0]
            manufacturers.append(manufacturer)
        return manufacturers

    @classmethod
    def select_by_id(cls, id, db=None):
        """
        Select a manufacturer by its id
        :param id: int
        :param db: Database
        :returns: name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer WHERE id = ?", (id,))
        return cls(data[0][1], data[0][2], data[0][3]) if data else None

    @classmethod
    def select_by_name(cls, name, db=None):
        """
        Select a manufacturer by its name
        :param name: str
        :param db: Database
        :returns: id, name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer WHERE name = ?", (name.lower(),))
        return cls(data[0][1], data[0][2], data[0][3]) if data else None

    @classmethod
    def select_by_factory_code(cls, factory_code, db=None):
        """
        Select a manufacturer by its factory code
        :param factory_code: int
        :param db: Database
        :returns: id, name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer WHERE factory_code = ?", (factory_code,))
        return cls(data[0][1], data[0][2], data[0][3]) if data else None
    
    @classmethod
    def select_by_partial_name(cls, name, db=None):
        """
        Select a manufacturer by its partial name
        :param
            name: str
            db: Database

        :returns: id, name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer WHERE name LIKE ?", (f"{name.lower()}%",))
        return data if data else ()
    
    @classmethod
    def select_by_partial_factory_code(cls, factory_code, db=None):
        """
        Select a manufacturer by its partial factory code
        :param
            factory_code: str
            db: Database

        :returns: id, name, description, factory_code
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM manufacturer WHERE factory_code LIKE ?", (f"{factory_code}%",))
        return data if data else ()
    
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
    def factory_code(self):
        return self._factory_code
    
    @factory_code.setter
    @_general_update_last_modified
    def factory_code(self, value):
        if not value:
            raise ValueError("Factory code cannot be empty")
        elif not isinstance(value, int):
            raise TypeError("Factory code must be an int")
        elif len (str(value)) < 0 or len(str(value)) > 4:
            raise ValueError("Factory code must be between 0 and 4 characters long")
        
        self._factory_code = value

    @property
    def last_update(self):
        return self._last_update