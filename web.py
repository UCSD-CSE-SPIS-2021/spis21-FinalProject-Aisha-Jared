
# python web.py

import os
from flask import Flask, url_for, render_template, request

import random

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home2.html')

@app.route('/randomizer')
def render_random_rest():
    return render_template('randomizer.html')

@app.route('/randomizer-result')
def render_random_rest_result():
    try:
        filter_result = request.args['filter']
        category_result = request.args['category']
        restaurant_result = random_rest(filter_result, category_result)
        return render_template('randomizer_result.html', restaurant = restaurant_result)
    except ValueError:
        return "Sorry, something went wrong :("

"""
@app.route('/review')
def render_review():
    return render_template('review.html')

@app.route('/review-result')
def render_review_result():
    try:
        r_result = request.args['answer']
        answer_result = review(r_result)
        return render_template('review_result.html')
    except ValueError:
        return "Sorry: something went wrong."
"""    

def random_rest(dietary_filter, category):

    # vegan
    if dietary_filter == 'vegan':
        if category == 'none':
            vegan_list = ["Blue Bowl", "Blue Pepper Asian Cuisine", "Caroline's Seaside Cafe", "Plant Power", "Roots", "The Bistro", "The Food Co-op"]
            vegan = vegan_list
            return random.choice(vegan_list)
    
    # vegetarian
    if dietary_filter == 'vegetarian': 
        if category == 'none':
            vegetarian_list = ["64 Degrees", "Bella Vista", "Blue Pepper Asian Cuisine", "Cafe Ventanas", "Caroline's Seaside Cafe", "Cups Outdoor Cafe", "Fresh", "Pacific Cafe", "Shogun of La Jolla / Fusion Noodle Cafe", "The Bistro", "The Food Co-op", "Wolftown"]
            vegetarian = vegetarian_list
            return random.choice(vegetarian_list)
    
    # no dietary restrictions
    if dietary_filter == 'none':
        
        # fast food 
        if category == 'fast':
            fast_list = ["Burger King", "Jamba Juice", "Panda Express", "Rubio's", "Subway"]
            fast = fast_list
            return random.choice(fast_list)

        # coffee
        if category == 'coffee':
            coffee_list = ["Cafe Ole'", "Cups Coffee", "Fairbanks Coffee", "Java Coast Coffee Cart", "Muir Woods Coffee House", "Splash Cafe at Birch Aquarium", "Starbucks", "TEC Cafe", "The Art of Espresso", "Audrey's Cafe", "Canyon Vista Marketplace", "OceanView", "Pacific Cafe", "Pepper Canyon Market", "Sixth Market", "Volkan Coffee"]
            coffee = coffee_list
            return random.choice(coffee_list)
        
        # asian
        if category == 'asian':
            asian_list = ["Blue Pepper Asian Cuisine", "Cafe Ventanas", "Earl's", "Fan-Fan", "Lemongrass Farm Fresh Plates", "Makai", "Noodles", "Pacific Cafe", "Panda Express", "Pines", "Seed + Sprout", "Shogun of La Jolla / Fusion Noodle Cafe", "Tapioca Express", "The Bistro"]
            asian = asian_list
            return random.choice(asian_list)
        
        # mexican
        if category == 'mexican':
            mexican_list = ["Fusion Grill", "Pacific Cafe", "Rubio's", "Taco Villa", "Wolftown"]
            mexican = mexican_list
            return random.choice(mexican_list)

        # italian
        if category == 'italian':
            italian_list = ["Bella Vista", "Foodworx", "Soda & Swine"]
            italian = italian_list
            return random.choice(italian_list)

        # american
        if category == 'american':
            american_list = ["64 Degrees", "Burger King", "Cafe Ventanas", "Caroline's Seaside Cafe", "Club Med", "Crave", "Croutons", "Dirty Birds", "Fusion Grill", "OceanView", "Pacific Cafe", "Pines", "Rooftop", "Sixty-Four North", "Splash! Cafe", "Subway", "Zanzibar"]
            american = american_list
            return random.choice(american_list)

        # greek
        if category == 'greek':
            greek_list = ["Santorini Greek Island Grill"]
            greek = greek_list
            return random.choice(greek_list)

        # middle eastern
        if category == 'middleeastern':
            me_list = ["Tahini"]
            middleeastern = me_list
            return random.choice(me_list)
        
        # mongolian
        if category == 'mongolian':
            mongolian_list = ["Three-Sixty"]
            mongolian = mongolian_list
            return random.choice(mongolian_list)

        # dessert
        if category == 'dessert':
            dessert_list = ["Art of Espresso Cafe", "Audrey's Cafe", "Cafe Ole", "Cups Outdoor Cafe", "Muir Woods", "Roger's Market", "Starbucks", "Su Pan Bakery", "Volkan Coffee", "YogurtWorld"]
            dessert = dessert_list
            return random.choice(dessert_list)

    # no dietary filters or category filters
    if dietary_filter == 'none':
        if category == 'none':
            none_list = ["64 Degrees", "Art of Espresso Cafe", "Audrey's Cafe", "Bella Vista", "Blue Bowl", "Blue Pepper Asian Cuisine", "Burger King", "Cafe Ole", "Cafe Ventanas", "Caroline's Seaside Cafe", "Club Med", "Copa Vida Cafe", "Crave", "Croutons", "Cups", "Cups Outdoor Cafe", "Dirty Birds", "Earl's", "Fan-Fan", "Foodworx", "Fresh", "Fusion Grill", "Jamba Juice", "Lemongrass Farm Fresh Plates", "Makai", "Muir Woods", "Noodles", "OceanView", "Pacific Cafe", "Panda Express", "Pines", "Plant Power", "Roger's Market", "Rooftop", "Roots", "Rubio's", "Santorini Greek Island Grill", "Seed + Sprout", "Shogun of La Jolla / Fusion Noodle Cafe", "Showa Ramen", "Sixth-Four North", "Soda & Swine", "Splash! Cafe", "Starbucks", "Su Pan Bakery", "Subway", "Taco Villa", "Tahini", "Tapioca Express", "TEC Cafe", "The Bistro", "The Food Co-op", "Three-Sixty", "Volkan Coffee", "Wolftown", "YogurtWorld", "Zanzibar"]
            none = none_list
            return random.choice(none_list)



if __name__=="__main__":
    app.run(host='0.0.0.0')

