#  views/form_views/edit_product_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.inventory_controller import InventoryController
from controllers.category_controller import CategoryController
from controllers.company_controller import CompanyController

class EditProductWindow(QDialog):

    def __init__(self, product_id):
        super().__init__()

        self.product = None  # Initialize to None
        self._product_id = product_id

        uic.loadUi('design/add_product_form.ui', self)

        # Basic window Settings
        self.setWindowTitle("Sales Management - Edit Product")


        self._load_categories_select()
        self._load_companies_select()
        self._load_edit_product()

        # Connect buttons
        self.btnAdd.clicked.connect(self.edit_product)
        self.btnCancel.clicked.connect(self.reject)
    
    def _load_edit_product(self):
        """
        Load the product to edit
        """
        try:
            self.product = InventoryController.get_product("id", self._product_id)

            # Set input fields with the product's current data
            self.nameInput.setText(self.product.name)
            self.priceInput.setText(str(self.product.price))
            self.quantityInput.setText(str(self.product.quantity))

            # Set select fields with the product's current data
            self.categorySelect.setCurrentIndex(self.categorySelect.findData(self.product.category_id))
            self.companySelect.setCurrentIndex(self.companySelect.findData(self.product.manufacturer_id))

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error loading the product: {e}")
            logging.error(f"Error loading product: {e}")
    
        
    def _load_categories_select(self):
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
        
    def _load_companies_select(self):
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
        

    def edit_product(self):
        """
        Edit the product
        """
        name = self.nameInput.text()
        category_id = self.categorySelect.itemData(self.categorySelect.currentIndex())
        manufacturer_id = self.companySelect.itemData(self.companySelect.currentIndex())
        price = self.priceInput.text()
        quantity = self.quantityInput.text()
        
        try:
            self.product.id = self._product_id
            self.product.name = name
            self.product.category_id = category_id
            self.product.manufacturer_id = manufacturer_id
            self.product.price = float(price)
            self.product.quantity = int(quantity)
            
            InventoryController.edit_product(self.product)

            # Set select fields with the product's current data
            self.product.category_name = CategoryController.get_category("id", self.product.category_id).name
            self.product.company_name = CompanyController.get_company("id", self.product.manufacturer_id).name

            self.nameInput.clear()
            self.categorySelect.setCurrentIndex(0)
            self.companySelect.setCurrentIndex(0)
            self.priceInput.clear()
            self.quantityInput.clear()
            
            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Editing Product", str(e))
            logging.warning(f"Error editing product: {e}") 
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
            logging.error(f"Critical error editing product: {e}")