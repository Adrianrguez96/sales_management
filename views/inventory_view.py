from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

from views.form_views.add_product_view import AddProductWindow

class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/inventory_window.ui', self)

        # Connects the buttons
        self.addInventory.clicked.connect(self.open_add_product_window)
        self.searchInventory.clicked.connect(self.open_search_product_window)

    def open_add_product_window(self):
        self.add_product_window = AddProductWindow()  
        self.add_product_window.exec_()  

    def open_search_product_window(self):
        pass