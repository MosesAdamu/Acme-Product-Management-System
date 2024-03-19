from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_attributes():
    prod = Product('Test Product')
    assert prod.name == 'Test Product'
    assert prod.price == 10
    assert prod.weight == 20
    assert prod.flammability == 0.5


def test_product_methods():
    prod = Product('Test Product', price=20, weight=30, flammability=1.5)
    assert prod.stealability() == "Kinda stealable."
    assert prod.explode() == "...boom!"


def test_generate_products():
    products = generate_products()
    assert len(products) == 30
