# /utils/type.py

from datetime import datetime

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