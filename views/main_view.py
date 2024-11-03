from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from functools import partial
import logging

# Load the UI views
from views.inventory_view import InventoryView
from views.category_view import CategoryView
from views.client_view import ClientView
from views.company_view import CompanyView
from views.sale_view import SaleView

# Constants for the main window
PROGRAM_TITLE = "Sales Management"
WINDOW_SIZE = (800, 650)
ICON_PATH = "/design/images/logo-icon.ico"

class MainView(QMainWindow):
    def __init__(self):
        """
        Initializes the MainView class
        """
        super().__init__()

        self.init_ui()

        # Initialize views with future extensibility
        self.views = {
            "inventory": InventoryView(),
            "category": CategoryView(),
            "client": ClientView(),
            "company": CompanyView(),
            "sale": SaleView()
        }
        
        # Dictionary to track data loading status
        self.data_loaded = {view_name: False for view_name in self.views}

        # Add all views to the stacked widget and set the initial view
        self.add_views()
        self.set_view("home")  # Set to "home" initially

        self.setup_menu_signals()

    def init_ui(self):
        """
        Load UI settings and configurations.
        """
        uic.loadUi('design/main_window.ui', self)
        self.setup_window()

    def setup_window(self):
        """
        Configure main window properties.
        """
        self.setWindowTitle(f"{PROGRAM_TITLE} - Home")
        self.setFixedSize(*WINDOW_SIZE)
        self.setWindowIcon(QIcon(ICON_PATH))

    def add_views(self):
        """Add views to the stacked widget."""
        for view in self.views.values():
            self.content.addWidget(view)

    def setup_menu_signals(self):
        """
        Connect menu buttons to the respective views.
        """
        menu_buttons = {
            self.btnHome: "home",
            self.btnInventory: "inventory",
            self.btnCategory: "category",
            self.btnClient: "client",
            self.btnCompany: "company",
            self.btnSale: "sale"
        }

        for button, view_name in menu_buttons.items():
            button.clicked.connect(partial(self.set_view, view_name))

    def set_view(self, view_name):
        """
        Set the current view based on the view name.
        :param view_name: str
        """
        if view_name == "home":
            self.content.setCurrentIndex(0)  # Assuming index 0 is the home view
            self.setWindowTitle(f"{PROGRAM_TITLE} - {view_name.capitalize()}")
        elif view_name in self.views:
            view = self.views[view_name]

            if not self.data_loaded[view_name]:
                self.initialize_view_data(view, view_name)
                self.data_loaded[view_name] = True
            
            self.content.setCurrentWidget(view)
            self.setWindowTitle(f"{PROGRAM_TITLE} - {view_name.capitalize()}")
        else:
            logging.error(f"Invalid view name: {view_name}")
            raise ValueError(f"Invalid view name: {view_name}")

    def initialize_view_data(self, view, view_name):
        """
        Initialize data for a view if it has not been loaded yet.
        :param view: QWidget
        :param view_name: str
        """
        if view_name == "category":
            view.load_categories()
