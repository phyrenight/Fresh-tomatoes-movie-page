import media
import fresh_tomatoes
# main file contains all the movie files
	
Avatar = media.Movie("Avatar","http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY","Movie about an disable ex soldier, that is sent to another world to replace his brother.","2009")	

Avengers = media.Movie("Avengers",	"http://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
"https://www.youtube.com/watch?v=eOrNdBpGMv8","Earth's mightest heroes assemble.","2012")
	
good_will_hunting = media.Movie("Good Will Hunting","http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg","https://www.youtube.com/watch?v=nH9LZOXBMUE","A trouble young adult get the help he needs.", "1997")
	
Enders_game = media.Movie("Ender's Game","http://upload.wikimedia.org/wikipedia/en/thumb/8/8c/Ender%27s_Game_poster.jpg/220px-Ender%27s_Game_poster.jpg	","https://www.youtube.com/watch?v=2SRizeR4MmU","A child is choosen to be the next commander.","2013")


myMovies = [Avatar, Avengers, good_will_hunting, Enders_game]

fresh_tomatoes.open_movies_page(myMovies)

