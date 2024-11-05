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
    def get_category(select_type, value):
        """
        Get a category from the database

        :param
            select_type: str
            value: int

        :returns: Category
        """

        match select_type:
            case "id":
                return Category.select_by_id(value)
            case "name":
                return Category.select_by_name(value)
            case "creation_date":
                return Category.select_by_creation_date(value)
            case "last_update":
                return Category.select_by_last_update(value)
            case _:
                raise ValueError("Select type not found")
    
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
    def edit_category(category_data):
        """
        Edit a category in the database

        :param name: str
        :param description: str

        :returns: Category id
        """
        try:
            Category.update(category_data)
        except Exception as e:    
            raise e
    
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
