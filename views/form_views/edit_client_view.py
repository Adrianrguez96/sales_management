# /views/form_views/edit_client_view.py

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# Import the controller
from controllers.client_controller import ClientController

class EditClientWindow(QDialog):

    def __init__(self, client_id):
        super().__init__()

        self.client = None  # Initialize to None
        self._client_id = client_id

        uic.loadUi('design/add_client_form.ui', self)

        # Basic window Settings
        self.setWindowTitle("Sales Management - Edit Client")

        self._load_edit_client()

        # Connect buttons
        self.btnAdd.clicked.connect(self.edit_client)
        self.btnCancel.clicked.connect(self.reject)
    
    def _load_edit_client(self):
        """
        Load the client to edit
        """
        try:
            self.client = ClientController.get_client("id", self._client_id)
            self.nameInput.setText(self.client.name)
            self.emailInput.setText(self.client.email)
            self.phoneInput.setText(self.client.phone)
            self.addressInput.setText(self.client.address)

        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error loading the client: {e}")
            logging.error(f"Error loading client: {e}")
    
    def edit_client(self):
        """
        Edit the client
        """
        name = self.nameInput.text()
        email = self.emailInput.text()
        phone = self.phoneInput.text()
        address = self.addressInput.text()

        try:
            self.client.id = self._client_id
            self.client.name = name
            self.client.email = email
            self.client.phone = phone
            self.client.address = address
            
            ClientController.edit_client(self.client)

            self.nameInput.clear()
            self.emailInput.clear()
            self.phoneInput.clear()
            self.addressInput.clear()
            
            self.accept()

        except ValueError as e:
            MessageService.show_warning("Error Editing Client", str(e))
            logging.warning(f"Error editing client: {e}") 
        except Exception as e:
            MessageService.show_critical_warning("Critical Error", str(e))
            logging.error(f"Critical error editing client: {e}")