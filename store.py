import products
from typing import List


class Store:

    def __init__(self, all_products):
        self.products = all_products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        total_items = 0
        for product in self.products:
            total_items += product.get_quantity()

        return total_items


    def get_all_products(self) -> List[products.Product]:
        active_items = []
        for product in self.products:
            if product.is_active():
                active_items.append(product)

        return active_items


    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price

        return total_price

