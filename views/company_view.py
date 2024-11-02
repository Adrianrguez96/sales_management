# /views/company_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from views.form_views.add_category_view import AddCategoryWindow

class CompanyView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/company_window.ui', self)

        # Set button signals
        self.addCompany.clicked.connect(self.open_add_category_window)
        self.searchCompany.clicked.connect(self.open_search_category_window)

    def open_add_category_window(self):
        self.add_product_window = AddCategoryWindow()  
        self.add_product_window.exec_()  

    def open_search_category_window(self):
        pass
        print("Add company")