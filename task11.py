from pprint import pprint
from products import products

query = "iphone"
kichik_query = query.lower()

product_filter = list(filter(
    lambda p: kichik_query in p.get('name', '').lower(), 
    products
))

pprint(product_filter)