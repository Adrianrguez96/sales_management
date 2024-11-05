# /models/client.py

from datetime import datetime
from database.database import Database
from utils.type import Type

class Client:
    def __init__(self, name, email, phone, address=None, db=None):
        """
        Initializes a new client object

        :param name: str
        :param email: str
        :param phone: str
        :param address: str
        :param db: Database
        """
        self.name = name.lower()
        self.email = email.lower()
        self.phone = phone.lower()
        self.address = address.lower()
        self._creation_date = datetime.now()
        self._last_update = datetime.now()
        self._db = db or Database()

    def __repr__(self):
        return (f"Client(name={self._name}, email={self._email}, phone={self._phone}, address={self._address}, "
                f"creation_date={self._creation_date}, last_update={self._last_update})")
    
    def save(self):
        """
        Saves the client to the database

        :returns: current client id
        """
        last_id = self._db.execute_query(
            "INSERT INTO clients (name, email, phone, address) VALUES (?, ?, ?, ?)",
            (self._name, self._email, self._phone, self._address)
        )
        return last_id

    # Class methods

    @classmethod
    def select_all(cls, db=None):
        """
        Select all clients
        :param db: Database
        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients")
        
        clients = []
        for row in data:
            client = cls(row[1], row[2], row[3], row[4])
            client.id = row[0]
            clients.append(client)
        return clients

    
    @classmethod
    def select_by_id(cls, id, db=None):
        """
        Select a client by its id
        :param id: int
        :param db: Database
        :returns: name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE id = ?", (id,))
        return cls(data[0][1], data[0][2], data[0][3], data[0][4]) if data else None

    @classmethod
    def select_by_name(cls, name, db=None):
        """
        Select a client by its name
        :param name: str
        :param db: Database
        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE name = ?", (name.lower(),))
        return cls(data[0][1], data[0][2], data[0][3], data[0][4]) if data else None
    
    @classmethod
    def select_by_partial_name(cls, name, db=None):
        """
        Select a client by its partial name
        :param
            name: str
            db: Database

        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE name LIKE ?", (f"{name.lower()}%",))
        return data if data else ()
    
    @classmethod 
    def select_by_partial_email(cls, email, db=None):
        """
        Select a client by its partial email
        :param
            email: str
            db: Database

        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE email LIKE ?", (f"{email.lower()}%",))
        return data if data else ()
    
    @classmethod 
    def select_by_partial_phone(cls, phone, db=None):
        """
        Select a client by its partial phone
        :param
            phone: str
            db: Database

        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE phone LIKE ?", (f"{phone.lower()}%",))
        return data if data else ()
    
    @classmethod 
    def select_by_partial_address(cls, address, db=None):
        """
        Select a client by its partial address
        :param
            address: str
            db: Database

        :returns: id, name, email, phone, address
        """
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE address LIKE ?", (f"{address.lower()}%",))
        return data if data else ()
    
    @classmethod
    def select_by_creation_date(cls, date, db=None):
        """
        Select a client by its creation date
        :param 
            date: str
            db: Database

        :returns: id, name, email, phone, address
        """
        if not Type.is_date(date):
            raise ValueError("Date must be in the format YYYY-MM-DD")
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE date(creation_date) = date(?)", (date,))
        return data if data else ()
    
    @classmethod
    def select_by_last_update(cls, date, db=None):
        """
        Select a client by its last update date
        :param 
            date: str
            db: Database

        :returns: id, name, email, phone, address
        """
        if not Type.is_date(date):
            raise ValueError("Date must be in the format YYYY-MM-DD")
        
        db = db or Database()
        data = db.fetch_data("SELECT * FROM clients WHERE date(last_update) = date(?)", (date,))
        return data if data else ()
    
    @classmethod
    def update(cls, client_data, db=None):
        """
        Update a client in the database

        :param 
            client_data: Instance of Client containing the data to update
            db: Database connection (optional)
        """
        db = db or Database()
        query = """
        UPDATE clients SET
        name = CASE WHEN COALESCE(name, '') <> COALESCE(?, '') THEN ? ELSE name END,
        email = CASE WHEN COALESCE(email, '') <> COALESCE(?, '') THEN ? ELSE email END,
        phone = CASE WHEN COALESCE(phone, '') <> COALESCE(?, '') THEN ? ELSE phone END,
        address = CASE WHEN COALESCE(address, '') <> COALESCE(?, '') THEN ? ELSE address END
        WHERE id = ?
        """
        db.execute_query(query, (client_data.name, client_data.name, client_data.email, client_data.email, 
                                 client_data.phone, client_data.phone, client_data.address, client_data.address, client_data.id))
    
    @classmethod    
    def delete(cls, client_id, db=None):
        """
        Delete a client from the database

        :param 
            client_id: int
            db: Database
        """
        db = db or Database()
        delete_id = db.execute_query("DELETE FROM clients WHERE id = ?", (client_id,))    
        return delete_id

    
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
    def email(self):
        return self._email
    
    @email.setter
    @_general_update_last_modified
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        elif not Type.is_email(value):
            raise ValueError("Email must be a valid email address")
        
        self._email = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    @_general_update_last_modified
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        elif not Type.is_phone_number(value):
            raise ValueError("Phone must be a valid phone number")
        
        self._phone = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    @_general_update_last_modified
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        elif not isinstance(value, str):
            raise TypeError("Address must be a string")
        
        self._address = value

    @property
    def last_update(self):
        return self._last_update