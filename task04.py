from pprint import pprint
from products import products

variants_count_by_product = {}

for product in products:
    product_id = product['id']
    count = len(product.get('variants', [])) 
    variants_count_by_product[product_id] = count

pprint(variants_count_by_product)