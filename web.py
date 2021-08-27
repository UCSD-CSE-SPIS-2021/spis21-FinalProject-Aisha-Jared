
import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/randomizer')
def render_random_rest():
    return render_template('randomizer.html')

@app.route{'/randomizer-result'}
def render_random_rest_result()
    # code

@app.route('/review')
def render_review():
    return render_template('review.html')











if __name__=="__main__":
    app.run(host='0.0.0.0')



   