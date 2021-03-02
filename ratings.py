"""Restaurant rating lister."""

# write a function
# open the file 
# iterate through each line in the text file
# split each line into a list for each restaurant 
# make a dictionary (key = name, value = rating)
# return the ratings in alphabetical order  

def alphabetize_restaurant(filename):
    restaurant_reviews = open(filename)

    book_of_reviews = []
    for line in restaurant_reviews:
        reviews = line.rstrip()
        reviews_list = reviews.split(":")
        book_of_reviews.append(reviews_list)
    
    dictionary_reviews = {}
    for review in book_of_reviews: 
        dictionary_reviews[review[0]] = review[1]

    dictionary_reviews = sorted(dictionary_reviews.items())
    
    for restaurant_name in dictionary_reviews:
        print(f"{restaurant_name[0]} is rated at {restaurant_name[1]}.")
        


alphabetize_restaurant("scores.txt")


