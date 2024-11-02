from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

# Import the controller
from controllers.category_controller import CategoryController

class AddCategoryWindow(QDialog):

    category_added = pyqtSignal(str, str)

    def __init__(self):
        """
        Initializes the AddCategoryWindow class
        """
        super().__init__()
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


        category = CategoryController.add_category(name, description)

        if category:
            self.category_added.emit(name, description)
            self.accept()
