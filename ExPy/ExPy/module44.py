"""Product Search"""

import decimal
import json
import pretty

_JSON_PATH = 'module44.json'

def _load():
    """Read the configured products"""
    with open(_JSON_PATH) as jsonhandle:
        return json.load(jsonhandle)

def _save(document):
    """Save the parsed JSON document (dict)"""
    with open(_JSON_PATH, 'w') as jsonhandle:
        json.dump(document, jsonhandle, indent=4, sort_keys=True)

def _create_product(product_name):
    """Given a product name, prompt for the price and quantity
    Return a new product record
    { "name": (str), "price": (float), "quantity": (int) }
    """
    while True:
        try:
            product_price = float(input('What is the price for the item? '))
            break
        except ValueError:
            print('Enter a valid price')
    while True:
        try:
            product_quantity = int(input('What is the quantity of the item? '))
            break
        except ValueError:
            print('Enter a valid quantity')
    return {
        'name': product_name,
        'price': product_price,
        'quantity': product_quantity
    }

def ex44():
    """Read the configured products and allow the user to search the inventory"""
    document = _load()
    products = document['products']

    while True:
        product_name = input('What is the product name? ')
        product = [x for x in products if x['name'].lower() == product_name.lower()]
        if product:
            product = product[0]
            print('Name: {}'.format(product['name']))
            price = pretty.money(decimal.Decimal(product['price']))
            print('Price: {}'.format(price))
            print('Quantity on hand: {}'.format(product['quantity']))
        else:
            print('Sorry, that product was not found in our inventory.')
            add = input('Would you like to add it? ').lower() == 'y'
            if add:
                product = _create_product(product_name)
                products.append(product)
                _save(document)

if __name__ == '__main__':
    ex44()
