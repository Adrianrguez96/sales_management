# /views/inventory_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/inventory_window.ui', self)

        