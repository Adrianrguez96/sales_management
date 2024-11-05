# /views/category_view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from utils.message_service import MessageService    
from utils.table import Table
import logging   


# Import the controller and views
from controllers.category_controller import CategoryController
from views.form_views.add_category_view import AddCategoryWindow
from views.form_views.edit_category_view import EditCategoryWindow
from views.form_views.search_view import SearchWindow
from views.context_menu_view import ContextMenuView

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

        # Set context menu signals
        self.categoryTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.categoryTable.customContextMenuRequested.connect(self._context_menu_category_table)
    
    def load_categories(self):
        """ 
        Load categories from the database 
        """
        try:
            categories = CategoryController.get_categories()
            Table.clear(self.categoryTable)
            for category in categories:
                Table.add_row(self.categoryTable, (category.name, category.description), extra_data=category.id)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the categories") 
            logging.error(f"Error loading categories: {e}")

    def _context_menu_category_table(self, pos):
        """
        Shows the context menu for the specified QTableWidget.
        
        :param pos: 
            Position of the right-click on the table
        """
        options = {
            "Edit Category": self.edit_category,
            "Delete Category": self.delete_category
        }

        try: 
            ContextMenuView.show_context_menu_table(self.categoryTable, pos, options)
            logging.info("Context menu category table shown")

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error showing the context menu: {e}")
            logging.error(f"Error showing context menu: {e}")



    def open_add_category_window(self):
        """ 
        Open the add category window 
        """
        self.add_category_window = AddCategoryWindow()

        if self.add_category_window.exec_() == QDialog.Accepted:
            results = self.add_category_window.results
            Table.add_row(self.categoryTable, (results[1], results[2]), extra_data = results[0])

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
                Table.add_row(self.categoryTable, (category[1], category[2]), extra_data=category[0])
            
            logging.info("Search results found")

    
    def edit_category(self,row_position):
        """
        Edit the category at the specified row position.
        
        :param row_position: int
        """
        item = self.categoryTable.item(row_position, 0)
        category_id = item.data(Qt.UserRole)  # Get the stored ID

        try:
            self.edit_category_window = EditCategoryWindow(category_id)

            if self.edit_category_window.exec_() == QDialog.Accepted:
                category_data = self.edit_category_window.category
                Table.update_row(self.categoryTable, row_position, (category_data.name, category_data.description), extra_data=category_data.id)
                logging.info(f"Category {category_data.name} edited successfully")
        
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error editing the category: {e}")
            logging.error(f"Error editing category: {e}")

    def delete_category(self,row_position):
        """
        Delete the category at the specified row position.
        
        :param row_position: int
        """
        item = self.categoryTable.item(row_position, 0)
        category_id = item.data(Qt.UserRole)  # Get the stored ID
        category_name = self.categoryTable.item(row_position, 0).text()

        is_deleted = MessageService.show_questions("Delete Category", f"Are you sure you want to delete the category '{category_name}'?")

        if is_deleted:
            try:
                CategoryController.delete_category(category_id)
                Table.delete_selected_row(self.categoryTable)
                logging.info(f"Category {category_name} deleted successfully")
            except Exception as e:
                MessageService.show_critical_warning("Error", f"There was an error deleting the category: {e}")
                logging.error(f"Error deleting category: {e}")