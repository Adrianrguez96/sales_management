# /views/company_view.py

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CompanyView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design/company_window.ui', self)