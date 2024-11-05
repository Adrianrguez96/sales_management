from PyQt5.QtWidgets import QTableWidget, QMenu


class ContextMenuView(object):

    @staticmethod
    def show_context_menu_table(table: QTableWidget,pos,options):
        """
        Shows the context menu for the specified QTableWidget.
        
        :param
            table: QTableWidget instance
        """

        row_position = table.rowAt(pos.y())  # Get the current row position

        if row_position >= 0:  

            context_menu = QMenu()  # Create a new QMenu instance

            for option_text, action_function in options.items():
                action = context_menu.addAction(option_text)  
                action.triggered.connect(lambda _, func=action_function: func(row_position))

            context_menu.exec_(table.viewport().mapToGlobal(pos))  

