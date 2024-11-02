# /views/category_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CategoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/category_window.ui', self)

        # Set view settings
        self.setWindowTitle("Sales Management - Categories")