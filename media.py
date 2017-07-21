import webbrowser


class Movie(object):
    """Movies class

    Attributes:
        title: The title of the movie
        storyline: A brief description of the movie
        poster_image_url: A hyperlink to the move poster
        trailer_youtube_url: A hyperlink to the youtube trailer
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
        self, movie_title, movie_storyline, poster_image, trailer_youtube
    ):
        """Inits a Movie obj with the given values

        Args:
            self: self
            movie_title: The title of the movie
            movie_storyline: A brief description of the movie
            poster_image: A hyperlink to the move poster
            trailer_youtube: A hyperlink to the youtube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Shows the movie's trailer at the URL stored in trailer_youtube_url

        Args:
            self: self
        """
        webbrowser.open(self.trailer_youtube_url)
