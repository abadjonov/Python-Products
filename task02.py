from pprint import pprint
from products import products

name_products = list(map
                       (lambda name: name.get("name"),
                         products))

pprint(name_products)