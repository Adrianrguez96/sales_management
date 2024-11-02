# /views/category_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from views.form_views.add_category_view import AddCategoryWindow

class CategoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/category_window.ui', self)

        # Set button signals
        self.addCategory.clicked.connect(self.open_add_category_window)
        self.searchCategory.clicked.connect(self.open_search_category_window)

    def open_add_category_window(self):
        self.add_product_window = AddCategoryWindow()  
        self.add_product_window.exec_()  

    def open_search_category_window(self):
        pass