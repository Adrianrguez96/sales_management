# /views/inventory_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/inventory_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Inventory")

        # Set button signals
        self.addInventory.clicked.connect(self.add_product)
        self.searchInventory.clicked.connect(self.search_product)

    def add_product(self):
        print("Add product")

    def search_product(self):
        print("Search product")


        