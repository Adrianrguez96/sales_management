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
            category.save()
            return category
        except ValueError as e:
            raise e
    
    @staticmethod
    def get_categories():
        """
        Get all categories from the database

        :returns: list
        """
        return Category.select_all()