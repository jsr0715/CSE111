import random

    # Create a list of strings and assign
    # the list to a variable named words.
words = ["the", "a", "one", "two", "some", "many"]

    # Call the random.choice function which will choose
    # one string from the words list. Store the chosen
    # string in a variable named word.
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["the", "one",]
    else:
        words = ["some", "many",]


    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word