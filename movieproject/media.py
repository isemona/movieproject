import webbrowser
# the following is the code for class Movie
class Movie():
    # def __init__ is constructor used to create an instance or object or example as in creating a new memory (aka initializing)
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #these are called arguments to the init fuction
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # each unique intance variables contains: title, storyline, poster_image_url, trailer_youtube_url
    # self is not a Python keyword, BUT for the sake of consistency and readability for future debugging it is good to use self as a naming convention (which class broswer specifically looks for!).

def show_trailer(self): # this is an instance method
        webbrowser.open(self.trailer_youtube_url) # accessible vis self
    # this function aka method will open the movie trailer of each movie




