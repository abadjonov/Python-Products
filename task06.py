from pprint import pprint
from products import products

all_ratings = [
    review['rating'] 
    for product in products 
    for review in product.get('reviews', [])
]

pprint(all_ratings)