from pprint import pprint
from products import products

active_products = list(filter
                       (lambda prod: prod.get("is_active") == True,
                         products))

pprint(active_products)
