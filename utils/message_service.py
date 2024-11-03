# /utils/message_service.py

from PyQt5.QtWidgets import QMessageBox, QWidget

class MessageService(QWidget):

    @staticmethod
    def apply_style(app):
        """
        Apply the style to the application
        :param app: QApplication
        """
        app.setStyleSheet("""
        QMessageBox {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #444444;
        }
        QMessageBox QLabel {
            color: #ffffff;
        }
        QMessageBox QPushButton {
            background-color: #555555;
            color: #ffffff;
            border: none;
            padding: 5px;
            border-radius: 3px;
        }
        QMessageBox QPushButton:hover {
            background-color: #777777;
        }
        """)

    @staticmethod
    def show_error(title,message):
        """
        Show an error message
        :param
            title: str
            message: str
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    @staticmethod
    def show_info(title,message):
        """
        Show an info message
        :param 
            title: str
            message: str

        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    @staticmethod
    def show_warning(title,message):
        """
        Show a warning message
        :param
            title: str
            message: str
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @staticmethod
    def show_questions(title,message):
        """
        Show a confirm message
        :param
            title: str
            message: str
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.exec_()
        

    @staticmethod
    def show_critical_warning(title,message):
        """
        Show a critical warning message
        :param
            title: str
            message: str
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()