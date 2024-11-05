# /views/form_views/search_view.py

from PyQt5.QtWidgets import QDialog, QDateEdit
from PyQt5 import uic
from utils.message_service import MessageService
import logging

# controllers imports
from controllers.inventory_controller import InventoryController
from controllers.category_controller import CategoryController
from controllers.company_controller import CompanyController

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
        self.results = ()

        uic.loadUi('design/search_form.ui', self)

        # Basic windows Settings and title
        self.setWindowTitle(f"Sales Management - {self.search_type.capitalize()} Search")
        self._change_title_text(f"Search {self.search_type.capitalize()}")
        self._select_search_options(self.options)

        # Invisible date field 
        self.searchDateLabel.setVisible(False) 
        self.searchDateInput.setVisible(False)

        # Connects the selection of search options	
        self.searchSelect.currentIndexChanged.connect(self._on_selection_search_changed)

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

        general_options = ["Creation Date","Last Update"]

        if isinstance(options, list):
            self.searchSelect.addItems(option.capitalize() for option in options)
        else:
            general_options.insert(0, "Name")
        
        self.searchSelect.addItems(general_options)
    
    def _on_selection_search_changed(self):
        """
        Called when the search selection changes
        """
        select = self.searchSelect.currentText()
        is_date_selection = select in ["Creation Date", "Last Update"]

        self.searchDateLabel.setVisible(is_date_selection)
        self.searchDateInput.setVisible(is_date_selection)

        self.searchLabel.setVisible(not is_date_selection)
        self.searchInput.setVisible(not is_date_selection)


    def search(self):
        """
        Searches the database
        """

        # Get the search options
        search_options = self.searchSelect.currentText()
        search_input = self.searchInput.text() if not self.searchDateInput.isVisible() else self.searchDateInput.date().toString("yyyy-MM-dd")
        print(search_input)
        try:
            match self.search_type:
                case "inventory":
                    self.results = InventoryController.search_product(search_options,search_input)
                case "category":
                    self.results =CategoryController.search_category(search_options,search_input)
                case "company":
                    self.results =CompanyController.search_company(search_options,search_input)
                case _:
                    MessageService.show_critical_warning("Critical error","Search type not found")
                    logging.error(f"Search type {self.search_type} not found")

            self.accept()
            return self.results
        
        except ValueError as e:
            MessageService.show_warning("Error Searching", str(e))
        except Exception as e:
            MessageService.show_critical_warning("Critical error", str(e))

                
