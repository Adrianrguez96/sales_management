# /views/company_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CompanyView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/company_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Companies")

        # Set button signals
        self.addCompany.clicked.connect(self.add_company)
        self.searchCompany.clicked.connect(self.search_company)

    def add_company(self):
        print("Add company")

    def search_company(self):
        print("Search company")