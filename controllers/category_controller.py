from models.category import Category

class CategoryController:
    def __init__(self):
        pass

    def add_category(self, name, description):
        category = Category(name, description)
        category.save()
        return category