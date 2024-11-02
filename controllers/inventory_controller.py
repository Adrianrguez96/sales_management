# /controllers/inventory_controller.py

from models.product import Product

class InventoryController:
    def __init__(self):
        pass

    def add_product(self, name, category_id, manufacturer_id, price, quantity):
        product = Product(name, category_id, manufacturer_id, price, quantity)
        product.save()
        return product