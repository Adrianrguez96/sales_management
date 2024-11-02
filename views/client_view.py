# /views/client_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class ClientView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/client_window.ui', self)

        # Set button signals
        self.addClient.clicked.connect(self.open_add_client_window)
        self.searchClient.clicked.connect(self.open_search_client_window)

    def open_add_client_window(self):
        print("Add client")

    def open_search_client_window(self):
        print("Search client")