def alphabetize_restaurant(filename):
    """Restaurant rating lister."""

    restaurant_reviews = open(filename)

    book_of_reviews = []
    for line in restaurant_reviews:
        reviews = line.rstrip()
        reviews_list = reviews.split(":")
        book_of_reviews.append(reviews_list)
    
    dictionary_reviews = {}
    for review in book_of_reviews: 
        dictionary_reviews[review[0]] = review[1]

    new_restaurant = input("What is the name of your restaurant? > ")
    new_rating = int(input("What is the rating of your restaurant? > "))
    dictionary_reviews[new_restaurant] = new_rating
    
    dictionary_reviews = sorted(dictionary_reviews.items())
    
    for restaurant_name in dictionary_reviews:
        print(f"{restaurant_name[0]} is rated at {restaurant_name[1]}.")
        

alphabetize_restaurant("scores.txt")


