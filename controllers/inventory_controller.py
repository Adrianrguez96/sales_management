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
            product.id = product.save()

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
        if not search_input:
            raise ValueError("Search input cannot be empty")

        match search_option:
            case "Name":
                return Product.select_product_by_partial_name(search_input)
            case "Category":
                return Product.select_product_by_category(search_input)
            case "Company":
                return Product.select_product_by_company(search_input)
            case "Price":
                return Product.select_product_by_price(search_input)
            case "Quantity":
                return Product.select_product_by_quantity(search_input)
            case "Creation Date":
                return Product.select_product_by_creation_date(search_input)
            case "Last Update":
                return Product.select_product_by_last_update(search_input)
            case _:
                raise ValueError("Search option not found")
    
    @staticmethod
    def delete_product(product_id):
        """
        Delete a product from the database
        :param product_id: int
        """
        try:
            Product.delete(product_id)
        except Exception as e:
            raise e