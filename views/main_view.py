# /views/main_view.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
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
        self.init_ui()

        self.views = [InventoryView(), CategoryView(), ClientView(), CompanyView(), SaleView()]
        self.add_views()
        self.set_view(0)

        self.setup_menu_signals()

    def init_ui(self):
        """Load UI settings and configurations."""
        uic.loadUi('design/main_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Home")
        self.setFixedSize(800, 650)
        self.setWindowIcon(QIcon("/design/images/logo-icon.ico"))

    def add_views(self):
        """Add views to the stacked widget."""
        for view in self.views:
            self.content.addWidget(view)

    def setup_menu_signals(self):
        """Connect menu buttons to the respective views."""
        buttons = [self.btnHome, self.btnInventory, self.btnCategory, 
                   self.btnClient, self.btnCompany, self.btnSale]

        for index, button in enumerate(buttons):
            button.clicked.connect(lambda checked, idx=index: self.set_view(idx))

    def set_view(self, index):
        """Set the current view based on the index."""
        if 0 <= index < (len(self.views) + 1):  # Ensure index is valid
            self.content.setCurrentIndex(index)
