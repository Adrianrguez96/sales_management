# /views/main_view.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

# Load the UI views
from views.inventory_view import InventoryView
from views.category_view import CategoryView
from views.client_view import ClientView
from views.company_view import CompanyView
from views.sale_view import SaleView

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()  

        super(QMainWindow, self).__init__()
        uic.loadUi('design/main_window.ui', self)

        # Add the inventory view
        self.addViews()

        self.content.setCurrentIndex(6)
    
    def addViews(self):
        self.content.addWidget(InventoryView())
        self.content.addWidget(CategoryView())
        self.content.addWidget(ClientView())
        self.content.addWidget(CompanyView())
        self.content.addWidget(SaleView())



