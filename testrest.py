
import random

def random_rest(dietary_filter, category):

    # str(dietary_filter)
    # str(category)

    # dietary_filter.casefold()
    # category.casefold()

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
        
        # coffee
        if category == 'coffee':
            coffee_list = ["Cafe Ole'", "Cups Coffee", "Fairbanks Coffee", "Java Coast Coffee Cart", "Muir Woods Coffee House", "Splash Cafe at Birch Aquarium", "Starbucks", "TEC Cafe", "The Art of Espresso", "Audrey's Cafe", "Canyon Vista Marketplace", "OceanView", "Pacific Cafe", "Pepper Canyon Market", "Sixth Market", "Volkan Coffee"]
            coffee = coffee_list
            return random.choice(coffee_list)
        
        # asian
        if category == 'asian':
            asian_list = ["Blue Pepper Asian Cuisine", "Lemongrass Fresh Farm Plates", "Pines"]
            asian = asian_list
            return random.choice(asian_list)
        
        # mexican
        if category == 'mexican':
            mexican_list = ["Rubio's", "Su Pan Bakery", "Taco Villa"]
            mexican = mexican_list
            return random.choice(mexican_list)


# python testrest.py
print(random_rest('none', 'coffee'))
