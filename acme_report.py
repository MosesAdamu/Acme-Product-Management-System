import random
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(product_list):
    unique_names = set(product.name for product in product_list)
    avg_price = sum(product.price
                    for product in product_list) / len(
                        product_list)
    avg_weight = sum(product.weight
                     for product in product_list) / len(
                         product_list)
    avg_flammability = sum(product.flammability
                           for product in product_list) / len(
                               product_list)

    return len(unique_names), avg_price, avg_weight, avg_flammability


if __name__ == '__main__':
    products = generate_products()
    print(inventory_report(products))
