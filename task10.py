from pprint import pprint
from products import products

grouped_by_category = {}

for product in products:
    category_name = product.get('category', {}).get('name', 'Unknown')
    
    if category_name not in grouped_by_category:
       grouped_by_category[category_name] = []
        
    grouped_by_category[category_name].append(product)

pprint(grouped_by_category)