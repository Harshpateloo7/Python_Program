#Write correct Python code to complete the following tasks. Document all assumptions. Maximum marks will
#be given to solutions that use nested lists, i.e. lists that look like [ ["some"data"]. ["other"" data" l. Partial
#marks will be given for only using flat lists (1 dimensional lists like list=["flat" list"] ).
#In a loop prompt the user to enter the name of a movie they like, and how many stars they think the movie is
#between 1 and 5 inclusive. Take the integer number of stars and convert it to a string with that many "*"
#asterisks. Store both the movie name and the rating in a list, and store that list in a list called ratedMovies.
#ratedMovies will start empty and will be added to as the user enters pairs of data.
#When the user is finished entering data they will enter "done" for the movie name. Do not save "done" to your
#list. but instead print out the list of movies the user entered along with their ratings.
def get_movies_list():
    ratedMovies = []
    continue_input = True

    while continue_input:
        movie_name = input('Please Enter Movies Name (or "done" to quit): ')
        if movie_name == 'done':
            break
        
        # Assume user will only enter integer numbers as a rating
        movie_rating = int(input('How Many Stars(1-5): '))
        
        while movie_rating == 0 or movie_rating > 5:
            movie_rating = int(input('Please Enter Star Between 1-5: '))
            
        movie_stars = '*'*movie_rating
        ratedMovies.append([movie_name, movie_stars])
    print(ratedMovies)
    return ratedMovies

get_movies_list()