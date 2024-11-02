from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

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
        pass