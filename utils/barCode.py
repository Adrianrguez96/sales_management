import random

class BarCode:
    
    @staticmethod
    def generate_barcode(country_code, factory_code):
        """
        Generates a random barcode based on the given country and factory codes.

        :param country_code: Country code of the barcode.
        :param factory_code: Factory code of the barcode.
        
        Example:
            BarCode.generate_barcode("038", "001")
        """
        product_code = f"{random.randint(0, 99999):05d}"  # Generate a random 5-digit product code
        code = f"{country_code}{factory_code}{product_code}"  # Concatenate codes
        verification_digit = BarCode.calculate_verification_digit(code)  # Calculate verification digit
        return f"{code}{verification_digit}"  # Return the complete barcode

    @staticmethod
    def calculate_verification_digit(code):
        """
        Calculates the verification digit for the given code using the UPC-A standard.

        :param code: The barcode without the verification digit.
        :return: The calculated verification digit.
        """
        total = sum(int(digit) * (3 if index % 2 else 1) for index, digit in enumerate(code))  # Calculate the total
        return (10 - total % 10) % 10  # Return the verification digit
  