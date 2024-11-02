# /views/sale_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class SaleView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/sale_window.ui', self)