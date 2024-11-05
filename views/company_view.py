# /views/company_view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from utils.message_service import MessageService
from utils.table import Table
import logging

# Import the controller and views
from controllers.company_controller import CompanyController
from views.form_views.add_company_view import AddCompanyWindow
from views.form_views.edit_company_view import EditCompanyWindow
from views.form_views.search_view import SearchWindow
from views.context_menu_view import ContextMenuView

class CompanyView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/company_window.ui', self)

        # Set context menu signals
        self.companyTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.companyTable.customContextMenuRequested.connect(self._context_menu_company_table)

        # Set button signals
        self.addCompany.clicked.connect(self.open_add_company_window)
        self.searchCompany.clicked.connect(self.open_search_company_window)
    
    def load_companies(self):
        """ 
        Load companies from the database 
        """
        try:
            companies = CompanyController.get_companies()
            Table.clear(self.companyTable)
            for company in companies:
                Table.add_row(self.companyTable, (company.name, company.description, company.factory_code), extra_data=company.id)
                
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the companies")
            logging.error(f"Error loading companies: {e}")
    
    def _context_menu_company_table(self, pos):
        """
        Shows the context menu for the specified QTableWidget.
        
        :param 
             pos: Position of the right-click on the table
        """
        options = {
            "Edit Company": self.edit_company,
            "Delete Company": self.delete_company
        }
        try: 
            ContextMenuView.show_context_menu_table(self.companyTable, pos, options)
            logging.info("Context menu company table shown")    
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error showing the context menu: {e}")
            logging.error(f"Error showing context menu: {e}")

    def open_add_company_window(self):
        self.add_product_window = AddCompanyWindow()

        if self.add_product_window.exec_() == QDialog.Accepted:
            results = self.add_product_window.results
            Table.add_row(self.companyTable, (results[1], results[2], results[3]) , extra_data = results[0])

    def open_search_company_window(self):
        """
        Open the search company window
        """
        self.search_company_window = SearchWindow("company",["name","factory code"])

        if self.search_company_window.exec_() == QDialog.Accepted:
            result = self.search_company_window.results

            if not result:
                MessageService.show_warning("No results found", "No companies found with the given search options")
                logging.info("No results found")
                return
            
            Table.clear(self.companyTable)
            for company in result:
                Table.add_row(self.companyTable, (company[1], company[2], company[3]), extra_data=company[0])
            
            logging.info("Search results found")

    def edit_company(self,row_position):
        """
        Edit the company at the specified row position.
        
        :param row_position: int
        """
        item = self.companyTable.item(row_position, 0)
        company_id = item.data(Qt.UserRole)  # Get the stored ID

        try:    
            self.edit_company_window = EditCompanyWindow(company_id)

            if self.edit_company_window.exec_() == QDialog.Accepted:
                company_data = self.edit_company_window.company
                Table.update_row(self.companyTable, row_position, (company_data.name, company_data.description, company_data.factory_code), extra_data=company_data.id)
                logging.info(f"Company {company_data.name} edited successfully")
        
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error editing the company: {e}")
            logging.error(f"Error editing company: {e}")
        
    def delete_company(self,row_position):
        """
        Delete the company at the specified row position.
        
        :param row_position: int
        """
        item = self.companyTable.item(row_position, 0)
        company_id = item.data(Qt.UserRole)  # Get the stored ID
        company_name = self.companyTable.item(row_position, 0).text()

        is_deleted = MessageService.show_questions("Delete Company", f"Are you sure you want to delete the company '{company_name}'?")

        if is_deleted:
            try:
                CompanyController.delete_company(company_id)
                Table.delete_selected_row(self.companyTable)
                logging.info(f"Company {company_name} deleted successfully")
            except Exception as e:
                MessageService.show_critical_warning("Error", f"There was an error deleting the company: {e}")
                logging.error(f"Error deleting company: {e}")