# /utils/table.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class Table:

    @staticmethod 
    def add_row(table: QTableWidget, data: tuple, extra_data = None):
        """
        Adds a new row to the specified QTableWidget.
        
        :param 
            table: QTableWidget instance
            data: tuple
            extra_data: optional data (e.g., ID or QDate) to associate with the row, hidden from view
        """

        row_position = table.rowCount()  # Get the current row position
        table.insertRow(row_position)  # Add a new row

        for i, value in enumerate(data):  # Iterate over the data and set the values
            table.setItem(row_position, i, QTableWidgetItem(str(value)))  # Set the value

        if extra_data is not None:
            table.item(row_position, 0).setData(Qt.UserRole, extra_data)

    @staticmethod
    def update_row(table: QTableWidget, row_position, data: tuple, extra_data = None):
        """
        Updates the data of the specified row in the specified QTableWidget.
        
        :param 
            table: QTableWidget instance
            row_position: int
            data: tuple
            extra_data: optional data (e.g., ID or QDate) to associate with the row, hidden from view
        """

        for i, value in enumerate(data):  # Iterate over the data and set the values
            table.setItem(row_position, i, QTableWidgetItem(str(value)))  # Set the value

        if extra_data is not None:
            table.item(row_position, 0).setData(Qt.UserRole, extra_data)
    
    @staticmethod
    def clear(table: QTableWidget):
        """
        Clears all data from the specified QTableWidget.
        
        :param table: QTableWidget instance
        """

        table.setRowCount(0)  # Set the number of rows to 0
        table.clearContents()  # Clear the content of the table (optional)
    
    @staticmethod
    def delete_selected_row(table: QTableWidget):
        """
        Deletes the currently selected row in the specified QTableWidget.
        
        :param table: QTableWidget instance
        """
        current_row = table.currentRow()  # Get the currently selected row
        
        if current_row >= 0:  # Check if a row is selected
            table.removeRow(current_row)  # Delete the selected row
        else:
            raise ValueError("No row selected")  # Raise an error if no row is selected
