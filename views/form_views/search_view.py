# /views/form_views/search_view.py

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import uic

class SearchWindow(QDialog):
    def __init__(self,search_type,options = "name"):
        """
        Initializes the SearchWindow class

        :param
            search_type: str
            options: str or list
        """
        super().__init__()

        self.search_type = search_type
        self.options = options

        uic.loadUi('design/search_form.ui', self)

        # Basic windows Settings and title
        self.setWindowTitle(f"Sales Management - {self.search_type.capitalize()} Search")
        self._change_title_text(f"Search {self.search_type.capitalize()}")
        self._select_search_options(self.options)

        # Connects buttons
        self.btnSearch.clicked.connect(self.search)
        self.btnCancel.clicked.connect(self.reject)
    
    def _change_title_text(self,text):
        """
        Change the title text

        :param text: str
        """
        html_title = self.searchTitle.toHtml()
        new_html_title = html_title.replace('Search',text)
        self.searchTitle.setHtml(new_html_title)
    
    def _select_search_options(self,options):
        """
        Select search options

        :param options: str or list
        """

        if isinstance(options, list):
            self.searchSelect.addItems(option.capitalize() for option in options)
        
        self.searchSelect.addItems(["Creation Date","Last Update"])

    def search(self):
        print("Search")
        self.accept()