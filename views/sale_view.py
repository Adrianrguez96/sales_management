# /views/sale_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class SaleView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/sale_window.ui', self)

        # Set button signals
        self.addSale.clicked.connect(self.open_add_sale_window)
        self.searchSale.clicked.connect(self.open_search_sale_window)

    def open_add_sale_window(self):
        print("Add sale")

    def open_search_sale_window(self):
        print("Search sale")