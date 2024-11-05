# /views/client_view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic
from utils.message_service import MessageService
from utils.table import Table
import logging 

# Import the controller and views
from controllers.client_controller import ClientController
from views.form_views.add_client_view import AddClientWindow
from views.form_views.edit_client_view import EditClientWindow
from views.form_views.search_view import SearchWindow
from views.context_menu_view import ContextMenuView

class ClientView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/client_window.ui', self)

        # Set button signals
        self.addClient.clicked.connect(self.open_add_client_window)
        self.searchClient.clicked.connect(self.open_search_client_window)
    
    def load_clients(self):
        """
        Load clients from the database
        """
        try:
            clients = ClientController.get_clients()
            for client in clients:
                Table.add_row(self.clientTable, (client.name, client.email, client.phone, client.address), extra_data=client.id)
        
        except Exception as e:
            MessageService.show_critical_warning("Error", "There was an error loading the clients") 
            logging.error(f"Error loading clients: {e}")
        
    def _context_menu_client_table(self, pos):
        """
        Shows the context menu for the specified QTableWidget.
        
        :param 
             pos: Position of the right-click on the table
        """
        options = {
            "Edit Client": self.edit_client,
            "Delete Client": self.delete_client
        }
        try: 
            ContextMenuView.show_context_menu_table(self.clientTable, pos, options)
            logging.info("Context menu client table shown")    
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error showing the context menu: {e}")
            logging.error(f"Error showing context menu: {e}")

    def open_add_client_window(self):
        """
        Open the add client window
        """
        self.add_client_window = AddClientWindow()

        if self.add_client_window.exec_() == QDialog.Accepted:
            results = self.add_client_window.results
            Table.add_row(self.clientTable, (results[1], results[2], results[3], results[4]))

    def open_search_client_window(self):
        """
        Open the search client window
        """
        self.search_client_window = SearchWindow("client",["name","creation date","last update"])

        if self.search_client_window.exec_() == QDialog.Accepted:
            result = self.search_client_window.results

            if not result:
                MessageService.show_warning("No results found", "No clients found with the given search options")
                logging.info("No results found")
                return
            
            Table.clear(self.clientTable)
            for client in result:
                Table.add_row(self.clientTable, (client[1], client[2], client[3], client[4]))
            
            logging.info("Search results found")



    def edit_client(self,row_position):
        """
        Edit the client at the specified row position.
        
        :param row_position: int
        """
        item = self.clientTable.item(row_position, 0)
        client_id = item.data(Qt.UserRole)  # Get the stored ID

        try:    
            self.edit_client_window = EditClientWindow(client_id)

            if self.edit_client_window.exec_() == QDialog.Accepted:
                client_data = self.edit_client_window.client
                Table.update_row(self.clientTable, row_position, (client_data.name, client_data.email, client_data.phone, client_data.address), extra_data=client_data.id)
                logging.info(f"Client {client_data.name} edited successfully")
        
        except Exception as e:
            MessageService.show_critical_warning("Error", f"There was an error editing the client: {e}")
            logging.error(f"Error editing client: {e}")
    
    def delete_client(self,row_position):
        """
        Delete the client at the specified row position.
        
        :param row_position: int
        """
        item = self.clientTable.item(row_position, 0)
        client_id = item.data(Qt.UserRole)  # Get the stored ID
        client_name = self.clientTable.item(row_position, 0).text()

        is_deleted = MessageService.show_questions("Delete Client", f"Are you sure you want to delete the client '{client_name}'?")

        if is_deleted:
            try:
                ClientController.delete_client(client_id)
                Table.delete_selected_row(self.clientTable)
                logging.info(f"Client {client_name} deleted successfully")
            except Exception as e:
                MessageService.show_critical_warning("Error", f"There was an error deleting the client: {e}")
                logging.error(f"Error deleting client: {e}")
