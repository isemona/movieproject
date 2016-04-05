import webbrowser

# the following is the code for class Movie
class Movie():
    """This class is a blueprint to display: movie title, storyline, poster image, and the trailer youtube that is unique to each movie.
    """
    # def __init__ is constructor used to create an instance or object or example as in creating a new memory (aka initializing).
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # These are called arguments to the init function.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # Self is not a Python keyword, BUT for the sake of consistency and readability for future debugging it is good to use self as a naming convention (which class broswer specifically looks for!).

# This is an instance method.
def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) # Accessible via self.
    """This function aka method will open the movie trailer of each movie."""




