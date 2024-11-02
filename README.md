# Sales Management

<div align="center"><img src="https://i.ibb.co/JzssR2q/logo-project.png" alt="Logo project"></div>

# Sales Management

Sales Management is a robust and user-friendly Python application designed to streamline retail operations by managing sales, products, categories, clients, and manufacturers. Built with the latest version of Python and utilizing the Qpython library for an intuitive graphical user interface (GUI), this system provides an efficient way to handle various aspects of a retail business. 

With its integrated SQLite3 database, Sales Management ensures reliable data storage and retrieval, making it easy to keep track of your inventory and sales data. Additionally, the program generates realistic barcodes for each product, enhancing the efficiency of inventory management and sales processing.

## Features

- **Product Categories Management**: Easily create, modify, and delete product categories to maintain an organized catalog.
- **Client Management**: Add, update, and remove client information, ensuring accurate records for sales and marketing.
- **Manufacturer Management**: Manage manufacturer details, including the ability to create, modify, and delete records.
- **Sales Management**: Efficiently track and manage sales transactions within the store.
- **Realistic Barcode Generation**: Each product includes a realistic barcode, generated using a specific factory code assigned to each manufacturer, reflecting real-world practices.

## System Requirements

- **Python**: The latest version of Python is required to run the application.
- **Qpython Library**: This application utilizes the Qpython library for GUI components.
- **SQLite3**: Built-in support for SQLite3 is used for database management.
- **Barcode Generation Library**: A barcode generation library is employed to create realistic barcodes for products.

## Installation

1. Ensure you have the latest version of Python installed on your machine.
2. Install the required libraries using pip:
   ```bash
   pip install qpython
   pip install python-barcode
   ```
   
3. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/user/SalesManagement.git
   ```
4. Navigate to the project directory:
   ```bash
   cd SalesManagement
   ```
   
5. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Creating Categories:** Navigate to the categories section in the GUI to create a new category.
2. **Managing Clients:** Access the clients section to add or modify client information.
3. **Manufacturer Codes:** When adding a new manufacturer, input their factory code for accurate barcode generation.
4. **Generating Products:** Products can be generated with a unique barcode reflecting the associated manufacturer’s factory code.
   
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the developers of Qpython for creating a powerful library for Python GUI development.
- Special thanks to the maintainers of SQLite3 and the barcode generation library for their invaluable contributions.
- Inspired by real-world inventory and sales management systems.