from pprint import pprint
from products import products

average_ratings = {}
for product in products:
    reviews = product.get('reviews', [])
    
    if not reviews:
        average_ratings[product['id']] = None
    else:
        total_rating = sum(review['rating'] for review in reviews)
        count = len(reviews)
        avg = total_rating / count
        
        average_ratings[product['id']] = round(avg, 2)

pprint(average_ratings)