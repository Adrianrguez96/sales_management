# /views/category_view.py

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog
from PyQt5 import uic
from utils.message_service import MessageService    
from utils.table import Table
import logging   


# Import the controller and views
from controllers.category_controller import CategoryController
from views.form_views.add_category_view import AddCategoryWindow
from views.form_views.search_view import SearchWindow

class CategoryView(QWidget):
    def __init__(self):
        """
        Initializes the CategoryView class
        """
        super().__init__()
        uic.loadUi('design/category_window.ui', self)

        # Set button signals
        self.addCategory.clicked.connect(self.open_add_category_window)
        self.searchCategory.clicked.connect(self.open_search_category_window)
    
    def load_categories(self):
        """ 
        Load categories from the database 
        """
        try:
            categories = CategoryController.get_categories()
            for category in categories:
                Table.add_row(self.categoryTable, (category.name, category.description))
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the categories") 
            logging.error(f"Error loading categories: {e}")

            

    def open_add_category_window(self):
        """ 
        Open the add category window 
        """
        self.add_category_window = AddCategoryWindow()
        self.add_category_window.exec_()

    def open_search_category_window(self):
        """
        Open the search category window
        """

        self.search_category_window = SearchWindow("category")
        
        if self.search_category_window.exec_() == QDialog.Accepted:
            result = self.search_category_window.results

            if not result:
                MessageService.show_warning("No results found", "No categories found with the given search options")
                logging.info("No results found")
                return
            
            Table.clear(self.categoryTable)
            for category in result:
                Table.add_row(self.categoryTable, (category[1], category[2]))
            
            logging.info("Search results found")