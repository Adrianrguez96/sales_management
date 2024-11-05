from models.category import Category

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
            category_id = category.save()
            return category_id
        except Exception as e:
            raise e
    
    @staticmethod
    def get_categories():
        """
        Get all categories from the database

        :returns: list
        """
        return Category.select_all()
    
    @staticmethod
    def search_category(search_options, search_input):
        """
        Search for categories in the database

        :params
            search_options: list
            search_input: str

        :returns: list
        """

        if not search_input:
            raise ValueError("Search input cannot be empty")

        match search_options:
            case "Name":
                return Category.select_by_partial_name(search_input)
            case "Creation Date":
                return Category.select_by_creation_date(search_input)
            case "Last Update":
                return Category.select_by_last_update(search_input)
            case _:
                raise ValueError("Search option not found")
    
    @staticmethod
    def delete_category(category_id):
        """
        Delete a category from the database

        :param category_id: int
        """
        try:
            Category.delete(category_id)
        except Exception as e:
            raise e
