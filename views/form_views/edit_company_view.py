# /views/form_views/edit_company_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.company_controller import CompanyController

class EditCompanyWindow(QDialog):

    def __init__(self, company_id):
        super().__init__()

        self.company = None  # Initialize to None
        self._company_id = company_id

        uic.loadUi('design/add_company_form.ui', self)

        # Basic window Settings
        self.setWindowTitle("Sales Management - Edit Company")

        #Edit main title
        html_content = self.formTitle.toHtml()
        updated_html = html_content.replace("Add Company", "Edit Company")
        self.formTitle.setHtml(updated_html)

        self._load_edit_company()

        # Connect buttons
        self.btnAdd.clicked.connect(self.edit_company)
        self.btnCancel.clicked.connect(self.reject)
    
    def _load_edit_company(self):
        """
        Load the company to edit
        """
        try:
            self.company = CompanyController.get_company("id", self._company_id)
            self.nameInput.setText(self.company.name)
            self.descriptionInput.setText(self.company.description)
            self.companyCodeInput.setText(str(self.company.factory_code))

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error loading the company: {e}")
            logging.error(f"Error loading company: {e}")
    
    def edit_company(self):
        """
        Edit the company
        """
        name = self.nameInput.text()
        description = self.descriptionInput.text()
        factory_code = int(self.companyCodeInput.text()) if self.companyCodeInput.text() else None

        try:
            self.company.id = self._company_id
            self.company.name = name
            self.company.description = description
            self.company.factory_code = factory_code
            
            CompanyController.edit_company(self.company)

            self.nameInput.clear()
            self.descriptionInput.clear()
            self.companyCodeInput.clear()
            
            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Editing Company", str(e))
            logging.warning(f"Error editing company: {e}") 
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))