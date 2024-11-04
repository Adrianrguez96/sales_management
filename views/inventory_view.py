# /views/inventory_view.py

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import uic
from utils.message_service import MessageService    
import logging 

# Import the controller and views
from controllers.inventory_controller import InventoryController
from views.form_views.add_product_view import AddProductWindow
from views.form_views.search_view import SearchWindow

class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/inventory_window.ui', self)

        # Connects the buttons
        self.addInventory.clicked.connect(self.open_add_product_window)
        self.searchInventory.clicked.connect(self.open_search_product_window)
    
    def load_products(self):
        """
        Load products from the database
        """
        try:
            products = InventoryController.get_products()
            for product in products:
                self.add_table_product(product['name'], product['category_name'], product['manufacturer_name'], product['price'], product['quantity'])
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the products") 
            logging.error(f"Error loading products: {e}")


    def open_add_product_window(self):
        """
        Open the add product window
        """
        self.add_product_window = AddProductWindow()
        self.add_product_window.product_added.connect(self.add_table_product)
        self.add_product_window.exec_()  

    def open_search_product_window(self):
        """
        Open the search product window
        """
        self.search_product_window = SearchWindow("inventory",["name","category","company","price","quantity"])
        self.search_product_window.exec_()

    def add_table_product(self, name, category, company, price, quantity):
        """
        Add a new row to the product table
        :param
            name: str
            category: str
            company: str
            price: float
            quantity: int
        """
        self.inventoryTable.setRowCount(self.inventoryTable.rowCount()+1)
        self.inventoryTable.setItem(self.inventoryTable.rowCount()-1,0,QTableWidgetItem(name))
        self.inventoryTable.setItem(self.inventoryTable.rowCount()-1,1,QTableWidgetItem(category))
        self.inventoryTable.setItem(self.inventoryTable.rowCount()-1,2,QTableWidgetItem(company))
        self.inventoryTable.setItem(self.inventoryTable.rowCount()-1,3,QTableWidgetItem(str(price)))
        self.inventoryTable.setItem(self.inventoryTable.rowCount()-1,4,QTableWidgetItem(str(quantity)))