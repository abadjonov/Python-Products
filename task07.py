from pprint import pprint
from products import products

variants = []
for product in products:
    variants.extend(product['variants'])

result = sorted(variants, key=lambda variant: variant['price'])

pprint(result)