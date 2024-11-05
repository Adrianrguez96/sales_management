# /views/form_views/edit_category_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.category_controller import CategoryController

class EditCategoryWindow(QDialog):

    def __init__(self, category_id):
        super().__init__()

        self.category = None  # Initialize to None
        self._category_id = category_id

        uic.loadUi('design/add_category_form.ui', self)

        # Basic window Settings
        self.setWindowTitle("Sales Management - Edit Category")

        self._load_edit_category()

        # Connect buttons
        self.btnAdd.clicked.connect(self.edit_category)
        self.btnCancel.clicked.connect(self.reject)
    
    def _load_edit_category(self):
        """
        Load the category to edit
        """
        try:
            self.category = CategoryController.get_category("id", self._category_id)
            self.nameInput.setText(self.category.name)
            self.descriptionInput.setText(self.category.description)

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error loading the category: {e}")
            logging.error(f"Error loading category: {e}")

    def edit_category(self):
        """
        Edit a category in the database
        """
        name = self.nameInput.text()
        description = self.descriptionInput.text()

        try:
            self.category.id = self._category_id
            self.category.name = name
            self.category.description = description
            
            CategoryController.edit_category(self.category)

            self.nameInput.clear()
            self.descriptionInput.clear()
            
            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Editing Category", str(e))
            logging.warning(f"Error editing category: {e}") 
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
            logging.error(f"Critical error editing category: {e}")
