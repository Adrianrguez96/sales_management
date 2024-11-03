from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import uic
from utils.message_service import MessageService    
import logging 

# Import the controller and views
from controllers.inventory_controller import InventoryController
from views.form_views.add_product_view import AddProductWindow

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
                self.add_table_product(product.name, product.category, product.company, product.price, product.quantity)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the products") 
            logging.error(f"Error loading products: {e}")


    def open_add_product_window(self):
        """
        Open the add product window
        """
        self.add_product_window = AddProductWindow()  
        self.add_product_window.exec_()  

    def open_search_product_window(self):
        pass

    def add_table_product(self, name, category, company, price, quantity):
        """
        Add a new row to the productTable
        :param
            name: str
            category: str
            company: str
            price: float
            quantity: int
        """
        self.productTable.setRowCount(self.productTable.rowCount()+1)
        self.productTable.setItem(self.productTable.rowCount()-1,0,QTableWidgetItem(name))
        self.productTable.setItem(self.productTable.rowCount()-1,1,QTableWidgetItem(category))
        self.productTable.setItem(self.productTable.rowCount()-1,2,QTableWidgetItem(company))
        self.productTable.setItem(self.productTable.rowCount()-1,3,QTableWidgetItem(str(price)))
        self.productTable.setItem(self.productTable.rowCount()-1,4,QTableWidgetItem(str(quantity)))