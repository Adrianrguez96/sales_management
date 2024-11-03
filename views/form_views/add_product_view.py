# /views/form_views/add_product_view.py

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from utils.message_service import MessageService 
import logging

# Import the controller
from controllers.category_controller import CategoryController
from controllers.company_controller import CompanyController
from controllers.inventory_controller import InventoryController

class AddProductWindow(QDialog):

    product_added = pyqtSignal(str, str, str, float, int)

    def __init__(self):
        super().__init__()
        uic.loadUi('design/add_product_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Product")

        # Load selectable categories and companies
        self.load_categories_select()
        self.load_companies_select()

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_product)
        self.btnCancel.clicked.connect(self.reject)

    def add_product(self):
        """
        Add a new product to the database
        """
        name = self.nameInput.text()
        category_id = self.categorySelect.itemData(self.categorySelect.currentIndex())
        manufacturer_id = self.companySelect.itemData(self.companySelect.currentIndex())
        price = self.priceInput.text()
        quantity = self.quantityInput.text()
        
        try:
            product = InventoryController.add_product(name, category_id, manufacturer_id, price, quantity)
            self.product_added.emit(product.name, product.category_name, product.manufacturer_name, product.price, product.quantity)
            self.accept()
        except ValueError as e:
            MessageService.show_warning("Error Adding Product", str(e))
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
    
    def load_categories_select(self):
        """
        Load categories from the database
        """
        self.categorySelect.clear()
        try:
            categories = CategoryController.get_categories()
            for category in categories:
                self.categorySelect.addItem(category.name, category.id)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the categories") 
            logging.error(f"Error loading categories: {e}")
        
    def load_companies_select(self):
        """
        Load categories from the database
        """
        self.companySelect.clear()
        try:
            companies = CompanyController.get_companies()
            for company in companies:
                self.companySelect.addItem(company.name, company.id)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the companies") 
            logging.error(f"Error loading companies: {e}")
        

    

