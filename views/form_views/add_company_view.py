from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from utils.message_service import MessageService

from controllers.company_controller import CompanyController

class AddCompanyWindow(QDialog):

    company_added = pyqtSignal(str, str, int)

    def __init__(self):
        """
        Initializes the AddCompanyWindow class
        """
        super().__init__()
        uic.loadUi('design/add_company_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Company")

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_company)
        self.btnCancel.clicked.connect(self.reject)

    def add_company(self):
        """
        Add a new company to the database
        """
        name = self.nameInput.text()
        description = self.descriptionInput.text()
        factory_code = int(self.companyCodeInput.text())

        try:
            CompanyController.add_company(name, description, factory_code)
            self.company_added.emit(name, description, factory_code)
            self.accept()
        except ValueError as e:
            MessageService.show_warning("Error Adding Company", str(e))
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))