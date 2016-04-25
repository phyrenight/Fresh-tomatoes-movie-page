import media
import fresh_tomatoes
import tmdbsimple as tmdb

tmdb.API_KEY = 'de4e5ffe351acf1b8fa71014d3feb8a6'
# main file contains all the movie files

# each will contain the title, movie
# poster, movie trailer, a brief
# description, and the year it was made.
# content will be entered in that order.
TMDBURL = "https://image.tmdb.org/t/p/w185"
YOUTUBEURL = "https://www.youtube.com/watch?v="
def get_movie_info(title):
    search = tmdb.Search()
    response = search.movie(query=title)

    movie = search.results[0]
    trailer = tmdb.Movies(movie['id']).videos()
    results = trailer['results'][0]
    video = YOUTUBEURL + results['key']
    poster = TMDBURL + movie['poster_path']
    return media.Movie(movie['title'],
                     poster,
                     video,
                     movie['overview'],
                     movie['release_date'])
    
#    movie = tmdb.Movies()


Avatar = get_movie_info('Avatar')
Avengers = get_movie_info('The Avengers')
good_will_hunting= get_movie_info('Good Will Hunting')
Enders_game = get_movie_info("Ender's Game")

myMovies = [Avatar, Avengers, good_will_hunting, Enders_game]

fresh_tomatoes.open_movies_page(myMovies)

