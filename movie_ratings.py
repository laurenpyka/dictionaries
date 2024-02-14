recommended_movies = []

def recommended_movie(movie_ratings, movie_title):
    if movie_title in movie_ratings:
        if movie_ratings[movie_title] >= 8:
            print(f"Based on its score, we recommend watching: {movie_title} \n")
        else:
            print("The movie title has a rating below 8, here are some other recommendations:\n")
            for movie, rating in movie_ratings.items():
                if rating >= 8:
                    recommended_movies.append(movie)
    else:
        print('The movie title entered was not found in the database')
        for movie, rating in movie_ratings.items():
            if rating >= 8:
                    recommended_movies.append(movie)
    
    for movie, rating in movie_ratings.items():
        if rating >= 8 and movie != movie_title:
            recommended_movies.append(f"{movie} : rating = {rating}")


    if recommended_movies:
        print("Reccomended movies:")
        for m in recommended_movies:
            print(m)

    else:
        print('There are no movies with a rating of 8 or higher.')


movie_ratings = {
    "Anyone But You": 7,
    "Just Go With It": 6, 
    "Mamma Mia": 9, 
    "21 Jump Street": 8,
    "Ferris Bueller's Day Off": 6
}


movie_title = input("Name a movie title: ")


recommended_movie(movie_ratings, movie_title)