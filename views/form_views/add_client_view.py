# /views/form_views/add_client_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.client_controller import ClientController

class AddClientWindow(QDialog):

    def __init__(self):
        """
        Initializes the AddClientWindow class
        """
        super().__init__()

        self.results = ()

        uic.loadUi('design/add_client_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Add Client")

        # Connects buttons
        self.btnAdd.clicked.connect(self.add_client)
        self.btnCancel.clicked.connect(self.reject)

    def add_client(self):
        """
        Add a new client to the database
        """
        name = self.nameInput.text()
        email = self.emailInput.text()
        phone = self.phoneInput.text()
        address = self.addressInput.text()

        try:
            client_id = ClientController.add_client(name, email, phone, address)
            self.results = (client_id,name, email, phone, address)

            self.nameInput.clear()
            self.emailInput.clear()
            self.phoneInput.clear()
            self.addressInput.clear()

            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Adding Client", str(e))
            logging.error(f"Error adding client: {e}")
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
            logging.critical(f"Error adding client: {e}")