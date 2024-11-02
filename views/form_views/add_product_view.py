from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

class AddProductWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/add_product_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Product")

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_product)
        self.btnCancel.clicked.connect(self.reject)

    def add_product(self):
        pass
        

