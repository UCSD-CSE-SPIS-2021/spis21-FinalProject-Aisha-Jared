
def review():

    answer = input(" Will you be going to the restaurant generated for you?:  ").casefold()

    if answer == "yes":
        review = input("Please write a quick review about your experience: ") 
        return("Thank you for your feedback.")

    if answer == "no":
        return("No worries, thank you!")

# python testrev.py
print(review())

#create a link on the home page that will allow user to submit review without having to ask whether they'll go or not 