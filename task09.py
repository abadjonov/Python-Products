from pprint import pprint
from products import products

max_prices_dict = {
    product['id']: (
        max(product.get('variants', []), 
            key=lambda x: x.get('price', 0))['price'] 
        if product.get('variants')
        else None
    )
    for product in products
}

pprint(max_prices_dict)