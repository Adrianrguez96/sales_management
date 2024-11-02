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

        if not name or not description:
            print("Category name and description cannot be empty")
            return None

        try:
        
            # Check if the category already exists
            if Category.select_by_name(name):
                print("Category already exists")
                return None
            
            category = Category(name, description)
            category.save()
            return category
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def get_categories():

        """
        Get all categories from the database

        :returns: list
        """

        return Category.select_all()