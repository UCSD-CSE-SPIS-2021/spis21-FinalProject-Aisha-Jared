
import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/randomizer')
def render_randomizer():
    return render_template('randomizer.html')





if __name__=="__main__":
    app.run(host='0.0.0.0')



   