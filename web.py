
import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def_


if __name__=="__main__":
    app.run(host='0.0.0.0')



def review():

    answer = input(" Will you be going to the restaurant generated for you?:  ")

    if answer == "yes":
        review = input("Please write a quick review about your experience: ")
        return("Thank you for your feedback.")

    if answer == "no":
        return("No worries, thank you!")


print(review())


   