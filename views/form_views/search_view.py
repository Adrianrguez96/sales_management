# /views/form_views/search_view.py

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

class SearchWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/search_form.ui', self)

        # Basic windows Settings
        self.setWindowTitle("Sales Management - Search")

        # Connects buttons
        self.btnSearch.clicked.connect(self.search)
        self.btnCancel.clicked.connect(self.reject)

    def search(self):
        print("Search")
        self.accept()