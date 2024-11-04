from models.category import Category
import logging

class CategoryController:

    @staticmethod
    def add_category(name, description):
        """
        Add a new category to the database.

        :params
            name: str
            description: str

        :returns: Category
        """

        # Check if the category already exists
        if Category.select_by_name(name):
            raise ValueError("Category already exists")
        try:
            category = Category(name, description)
            category.save()
            logging.info(f"Category {name} added successfully")
            return category
        except Exception as e:
            logging.error(f"Error adding category: {e}")
            raise e
    
    @staticmethod
    def get_categories():
        """
        Get all categories from the database

        :returns: list
        """
        return Category.select_all()
    
    @staticmethod
    def search_category(search_option, search_input):
        """
        Search for categories in the database

        :params
            search_options: list
            search_input: str

        :returns: list
        """
        print(search_option)