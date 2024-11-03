from database.database import Database
from PyQt5.QtWidgets import QApplication

from views.main_view import MainView
from utils.message_service import MessageService

if __name__ == "__main__": 
    db = Database()
    db.create_tables()

    app = QApplication([])

    MessageService.apply_style(app)

    main_view = MainView()
    main_view.resize(1000, 600)
    main_view.show() 
    
    app.exec_() 

