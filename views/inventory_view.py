# /views/inventory_view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from utils.message_service import MessageService
from utils.table import Table
import logging 

# Import the controller and views
from controllers.inventory_controller import InventoryController
from views.form_views.add_product_view import AddProductWindow
from views.form_views.edit_product_view import EditProductWindow
from views.form_views.search_view import SearchWindow
from views.context_menu_view import ContextMenuView

class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/inventory_window.ui', self)

        # Set context menu signals
        self.inventoryTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.inventoryTable.customContextMenuRequested.connect(self._context_menu_inventory_table)

        # Connects the buttons
        self.addInventory.clicked.connect(self.open_add_product_window)
        self.searchInventory.clicked.connect(self.open_search_product_window)
    
    def load_products(self):
        """
        Load products from the database
        """
        try:
            products = InventoryController.get_products()
            Table.clear(self.inventoryTable)
            for product in products:
                Table.add_row(self.inventoryTable, (product['name'], product['category_name'], 
                                                    product['manufacturer_name'], product['price'], product['quantity']), extra_data=product['id'])
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the products") 
            logging.error(f"Error loading products: {e}")

    def _context_menu_inventory_table(self, pos):
        """
        Shows the context menu for the specified QTableWidget.
        
        :param 
             pos: Position of the right-click on the table
        """
        options = {
            "Edit Product": self.edit_product,
            "Delete Product": self.delete_product
        }
        try: 
            ContextMenuView.show_context_menu_table(self.inventoryTable, pos, options)
            logging.info("Context menu inventory table shown")    
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error showing the context menu: {e}")
            logging.error(f"Error showing context menu: {e}")


    def open_add_product_window(self):
        """
        Open the add product window
        """
        self.add_product_window = AddProductWindow()

        if self.add_product_window.exec_()  == QDialog.Accepted:
            results = self.add_product_window.results
            Table.add_row(self.inventoryTable, (results[1], results[2], results[3], results[4], results[5]), extra_data = results[0])

    def open_search_product_window(self):
        """
        Open the search product window
        """
        self.search_product_window = SearchWindow("inventory",["name","category","company","price","quantity"])

        if self.search_product_window.exec_() == QDialog.Accepted:
            result = self.search_product_window.results

            if not result:
                MessageService.show_warning("No results found", "No products found with the given search options")
                logging.info("No results found")
                return
            Table.clear(self.inventoryTable)
            for product in result:
                Table.add_row(self.inventoryTable, (product[1], product[3], product[4], product[5], product[6]), extra_data=product[0])
            
            logging.info("Search results found")
    
    def edit_product(self,row_position):
        """
        Edit the product at the specified row position.
        
        :param row_position: int
        """
        item = self.inventoryTable.item(row_position, 0)
        product_id = item.data(Qt.UserRole)  # Get the stored ID

        try:    
            self.edit_product_window = EditProductWindow(product_id)

            if self.edit_product_window.exec_() == QDialog.Accepted:
                product_data = self.edit_product_window.product

                Table.update_row(self.inventoryTable, row_position, (product_data.name,product_data.category_name, 
                      product_data.company_name, product_data.price, 
                      product_data.quantity), extra_data=product_data.id)
                
                logging.info(f"Product {product_data.name} edited successfully")  

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error editing the product: {e}")
            logging.error(f"Error editing product: {e}")
        
    def delete_product(self,row_position):
        """
        Delete the product at the specified row position.
        
        :param row_position: int
        """
        item = self.inventoryTable.item(row_position, 0)
        product_id = item.data(Qt.UserRole)  # Get the stored ID        
        product_name = self.inventoryTable.item(row_position, 0).text()

        is_deleted = MessageService.show_questions("Delete Product", f"Are you sure you want to delete the product '{product_name}'?")

        if is_deleted:
            try:
                InventoryController.delete_product(product_id)
                Table.delete_selected_row(self.inventoryTable)
                logging.info(f"Product {product_name} deleted successfully")
            except Exception as e:
                MessageService.show_critical_warning("Error", f"There was an error deleting the product: {e}")
                logging.error(f"Error deleting product: {e}")

