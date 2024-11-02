from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

class AddComnpanyWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/add_company_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Company")

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_company)
        self.btnCancel.clicked.connect(self.reject)

    def add_company(self):
        pass