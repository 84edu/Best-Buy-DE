class Product:

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("The name must be given!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity

        if quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        if self.quantity < quantity:
            raise ValueError("Not enough in stock!")

        if not self.is_active():
            raise Exception("Product is not active!")

        total_price = self.price * quantity

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        return total_price

