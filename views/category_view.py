# /views/category_view.py

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import uic
from utils.message_service import MessageService       


# Import the controller and views
from controllers.category_controller import CategoryController
from views.form_views.add_category_view import AddCategoryWindow

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
                self.add_table_category(category.name, category.description)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the categories")  

            

    def open_add_category_window(self):
        """ 
        Open the add category window 
        """
        self.add_category_window = AddCategoryWindow()  
        self.add_category_window.category_added.connect(self.add_table_category)
        self.add_category_window.exec_()  

    def open_search_category_window(self):
        pass

    def add_table_category(self,name,description):
        """
        Add a new row to the categoryTable
        :param
            name: str
            description: str
        """
        self.categoryTable.setRowCount(self.categoryTable.rowCount()+1)
        self.categoryTable.setItem(self.categoryTable.rowCount()-1,0,QTableWidgetItem(name))
        self.categoryTable.setItem(self.categoryTable.rowCount()-1,1,QTableWidgetItem(description))