# /views/company_view.py

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from utils.message_service import MessageService
from utils.table import Table
import logging

# Import the controller and views
from controllers.company_controller import CompanyController
from views.form_views.add_company_view import AddCompanyWindow
from views.form_views.search_view import SearchWindow

class CompanyView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/company_window.ui', self)

        # Set button signals
        self.addCompany.clicked.connect(self.open_add_company_window)
        self.searchCompany.clicked.connect(self.open_search_company_window)
    
    def load_companies(self):
        """ 
        Load companies from the database 
        """
        try:
            companies = CompanyController.get_companies()
            for company in companies:
                Table.add_row(self.companyTable, (company.name, company.description, company.factory_code))
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the companies")
            logging.error(f"Error loading companies: {e}")

    def open_add_company_window(self):
        self.add_product_window = AddCompanyWindow()

        if self.add_product_window.exec_() == QDialog.Accepted:
            results = self.add_product_window.results
            Table.add_row(self.companyTable, (results[0], results[1], results[2]))

    def open_search_company_window(self):
        """
        Open the search company window
        """
        self.search_company_window = SearchWindow("company",["name","factory code"])
        self.search_company_window.exec_()