# /database/database.py

import sqlite3 as sql
from sqlite3 import Error

import logging
from utils.message_service import MessageService

class Database:
    def __init__(self, db_path="database/shop_db.db"):
        """
        Initializes the Database class

        :param
            db_path: str (default: "database/shop_db.db")
        """
        self._db_path = db_path

    def connection(self):
        """
        Returns a connection to the database

        :return connection: sqlite3.Connection
        """
        try:
            return sql.connect(self._db_path)
        except Error as e:
            MessageService.show_critical_warning("Internal Error", f"Error to connect to database")
            logging.critical(f"Error to connect to database: {e}")
            return None

    def create_tables(self):
        """
        Creates the tables in the database
        """
        try:
            with self.connection() as con:
                cursor = con.cursor()
                cursor.executescript(open("database/schema.sql").read())
                con.commit()
                logging.info("Tables have been created successfully")
        except FileNotFoundError:
            MessageService.show_critical_warning("Error", "Schema.sql file not found")
            logging.error("Schema.sql file not found")
        except Error as e:
            MessageService.show_critical_warning("Internal Error", "Error creating tables")
            logging.critical(f"Error to create tables: {e}")

    def create_triggers(self):
        """
        Creates the triggers in the database
        """
        try:
            with self.connection() as con:
                cursor = con.cursor()
                cursor.executescript(open("database/triggers.sql").read())
                con.commit()
                logging.info("Triggers have been created successfully")
        except FileNotFoundError:
            MessageService.show_critical_warning("Error", "Triggers.sql file not found")
            logging.error("Triggers.sql file not found")
        except Error as e:
            MessageService.show_critical_warning("Internal Error", "Error creating triggers")
            logging.critical(f"Error to create triggers: {e}")

    def execute_query(self, query, params=()):
        """
        Executes a single query against the database

        :param
            query: str
            params: tuple

        :returns: last inserted row id or None
        """
        try:
            with self.connection() as con:
                cursor = con.cursor()
                cursor.execute(query, params)
                con.commit()
                return cursor.lastrowid 
        except Error as e:
            MessageService.show_critical_warning("Internal Error", f"Error to consult database")
            logging.error(f"Error to execute query: {e}")
            return None

    def fetch_data(self, query, params=()):
        """
        Fetches data from the database based on a query

        :param
            query: str
            params: tuple
        
        :returns: cursor data or empty list
        """
        try:
            with self.connection() as con:
                cursor = con.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
        except Error as e:
            MessageService.show_critical_warning("Internal Error", f"Error to consult database")
            logging.error(f"Error to fetch data: {e}")
            return []