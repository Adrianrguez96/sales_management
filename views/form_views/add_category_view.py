# /views/form_views/add_category_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.category_controller import CategoryController

class AddCategoryWindow(QDialog):

    def __init__(self):
        """
        Initializes the AddCategoryWindow class
        """
        super().__init__()

        self.results = ()

        uic.loadUi('design/add_category_form.ui', self)

        self.setWindowTitle("Sales Management - Add Category")


        self.btnAdd.clicked.connect(self.add_category)
        self.btnCancel.clicked.connect(self.reject)

    def add_category(self):
        """
        Add a new category to the database
        """
        name = self.nameInput.text()
        description = self.descriptionInput.text()

        try:
            category_id = CategoryController.add_category(name, description)
            self.results = (category_id,name, description)

            self.nameInput.clear()
            self.descriptionInput.clear()  
            
            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Adding Category", str(e))
            logging.error(f"Error adding category: {e}")
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
            logging.critical(f"Error adding category: {e}")
        
