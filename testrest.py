
# filters: vegan, vegetarian, cafe

import random

def random_rest(dietary_filter, category):

    # vegan
    if dietary_filter == 'vegan':
        if category == 'none':
            vegan_list = ["Roots", "The Food Co-op", "Volkan Coffee"]
            vegan = vegan_list
            return random.choice(vegan_list)
    
    # vegetarian
    if dietary_filter == 'vegetarian': 
        if category == 'none':
            vegetarian_list = ["Blue Pepper Asian Cuisine", "Cups Outdoor Cafe", "The Bistro", "The Food Co-op"]
            vegetarian = vegetarian_list
            return random.choice(vegetarian_list)
    
    # no dietary restrictions
    if dietary_filter == 'none':
        
        # cafe
        if category == 'cafe':
            cafe_list = ["Cafe Ventanas", "Caroline's Seaside Cafe", "Splash! Cafe"]
            cafe = cafe_list
            return random.choice(cafe_list)
        
        # asian
        if category == 'asian':
            asian_list = ["Blue Pepper Asian Cuisine", "Lemongrass Fresh Farm Plates"]
            asian = asian_list
            return random.choice(asian_list)
        
        # mexican
        if category == 'mexican':
            mexican_list = []
    
# python testrest.py
print(random_rest('none', 'asian'))
