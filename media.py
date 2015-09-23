class Movie():
	def __init__(self, title, poster_image, movie_trailer,
                 description, year_made):
            self.title = title
            self.poster_image_url = poster_image
            self.trailer_youtube_url = movie_trailer
            self.description = description
            self.year_made = year_made
            # year_made will contain the year the movie hit the theaters
