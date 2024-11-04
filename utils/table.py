from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class Table:

    @staticmethod 
    def add_row(table: QTableWidget, data: tuple):
        """
        Adds a new row to the specified QTableWidget.
        
        :param 
            table: QTableWidget instance
            data: tuple
        """

        table.insertRow(table.rowCount())  # Add a new row

        for i, value in enumerate(data):  # Iterate over the data and set the values
            table.setItem(table.rowCount() - 1, i, QTableWidgetItem(str(value)))  # Set the value

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
