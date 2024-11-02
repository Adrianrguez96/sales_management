from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

from controllers.category_controller import CategoryController

class AddCategoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/add_category_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Category")

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_category)
        self.btnCancel.clicked.connect(self.reject)

    def add_category(self):
        name = self.nameInput.text()
        description = self.descriptionInput.text()
        
        category = CategoryController.add_category(name, description)

        if category:
            self.accept()

