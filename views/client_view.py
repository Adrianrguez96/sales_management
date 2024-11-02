# /views/client_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class ClientView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/client_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Clients")

        # Set button signals
        self.addClient.clicked.connect(self.add_client)
        self.searchClient.clicked.connect(self.search_client)

    def add_client(self):
        print("Add client")

    def search_client(self):
        print("Search client")