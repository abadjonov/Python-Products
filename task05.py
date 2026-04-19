from pprint import pprint
from products import products

active_products = list(filter
                       (lambda prod: prod.get("stock") == 0,
                         products))

pprint(active_products)
