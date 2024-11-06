# /utils/type.py

from datetime import datetime
import re

class Type:

    @staticmethod
    def is_float(value):
        """
        Check if the value is a number.

        :param value: any
        :returns: bool
        """
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def is_int(value):
        """
        Check if the value is an integer.

        :param value: any
        :returns: bool
        """
        try:
            int(value)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def is_date(value):
        """
        Check if the value is a date.

        :param value: any
        :returns: bool
        """
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    @staticmethod
    def is_email(value):
        """
        Check if the value is an email.

        :param value: any
        :returns: bool
        """
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, value)
    
    @staticmethod
    def is_phone_number(value):
        """
        Check if the value is a phone number.

        :param value: any
        :returns: bool
        """
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        
        pattern = r"^\+?[1-9]\d{1,14}$"
        return re.match(pattern, value)