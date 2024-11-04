# /controllers/inventory_controller.py

from models.product import Product
from models.category import Category
from models.company import Company
import logging

class InventoryController:

    @staticmethod
    def add_product(name, category_id, manufacturer_id, price, quantity):
        """
        Add a new product to the database

        :param 
            name: str
            category_id: int
            manufacturer_id: int
            price: float
            quantity: int
        
        :returns: Product
        """

        # Check if the product already exists
        if Product.select_by_name(name):
            raise ValueError("Product already exists")
        
        try:
            # TODO: Check message service error handling decimal or integer
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None

            product = Product(name, category_id, manufacturer_id, price, quantity)
            product.save()

            product.category_name = Category.select_by_id(category_id).name
            product.manufacturer_name = Company.select_by_id(manufacturer_id).name

            logging.info(f"Product {name} added successfully")
            return product
        except Exception as e:
            logging.error(f"Error adding product: {e}")
            raise e
    
    @staticmethod
    def get_products():
        """
        Get all products from the database
        :returns: list
        """
        products = Product.select_all()
        
        return products
    
    @staticmethod
    def search_product(search_option, search_input):
        """
        Search for products in the database

        :params
            search_options: list
            search_input: str

        :returns: list
        """
        print(search_option)