from pprint import pprint
from products import products

category_names = list(map(lambda prod: prod['category']['name'], products))
category_numbers = len(category_names)

pprint((category_numbers))
