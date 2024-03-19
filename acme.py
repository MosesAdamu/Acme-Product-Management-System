import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product_result = self.flammability * self.weight
        if product_result < 10:
            return "...fizzle."
        elif product_result < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


# Test code
if __name__ == '__main__':
    prod = Product('A Cool Toy')
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)
