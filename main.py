from database.database import Database
from PyQt5.QtWidgets import QApplication

from views.main_view import MainView
from utils.message_service import MessageService
from utils.logging_config import setup_logging

if __name__ == "__main__": 
    setup_logging("sales_management.log")
    
    db = Database()
    db.create_tables() # Create tables if they don't exist
    db.create_triggers() # Create triggers if they don't exist

    app = QApplication([])

    MessageService.apply_style(app)

    main_view = MainView()
    main_view.resize(1000, 600)
    main_view.show() 
    
    app.exec_() 

