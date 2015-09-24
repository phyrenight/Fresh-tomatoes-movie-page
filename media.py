class Movie():
    """This class can hold a
    movies information.The information
    it can contain is very limited.
    """
    def __init__(self, title, poster_image, movie_trailer,
                 description, year_made):
            """ This constructor method takes
            input for the title, poster image,
            a description, and the year the
            movie came out.It does not output anything.
            """
            self.title = title
            self.poster_image_url = poster_image
            self.trailer_youtube_url = movie_trailer
            self.description = description
            self.year_made = year_made
            # year_made will contain the year the movie hit the theaters
