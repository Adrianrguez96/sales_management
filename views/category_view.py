# /views/category_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CategoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/category_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Categories")

        # Set button signals
        self.addCategory.clicked.connect(self.add_category)
        self.searchCategory.clicked.connect(self.search_category)

    def add_category(self):
        print("Add category")

    def search_category(self):
        print("Search category")