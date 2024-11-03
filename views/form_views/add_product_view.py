from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
import logging
import utils.message_service as MessageService

# Import the controller
from controllers.category_controller import CategoryController
from controllers.company_controller import CompanyController

class AddProductWindow(QDialog):
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
        pass
    
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
        

    

