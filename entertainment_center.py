import fresh_tomatoes
import media

# Import fresh_tomatoes is starter that must be downloaded
# and added to the movie project folder.

# This the instance of the movie Big Hero it will showcase the arguments
# aka info: title, storyline, poster image, and youtube trailer.
big_hero = media.Movie(
                       "Big Hero 6",
                       "A story of a young robotics prodigy named Hiro Hamada who forms a"
                       "superhero team to combat a masked villain (Wikipedia).",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",  # noqa
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")  # noqa

# This the instance of the movie Amelie.
amelie = media.Movie(
                     "Amelie",
                     "Amelie is an innocent and naive girl in Paris with her own sense of"
                     "justice. She decides to help those around her and, along the way,"
                     "discovers love (Wikipedia).",
                     "http://cdn.miramax.com/media/assets/Amelie1.png",  # noqa
                     "http://www.magiclanternfilmsociety.org/wp-content/uploads/2012/06/Amelie.jpg")  # noqa

# This the instance of the movie Zootopia.
zootopia = media.Movie(
                       "Zootopia",
                       "The film details the unlikely partnership between a rabbit police officer"
                       "and a red fox con artist as they uncover a conspiracy that involves the"
                       "disappearance of predator civilians within a mammalian"
                       "utopia (Wikipedia).",
                       "http://vignette4.wikia.nocookie.net/disney/images/2/2f/Zootopia_Poster.jpg/revision/latest?cb=20151210185516",  # noqa
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")  # noqa

# This the instance of the movie The Fifth Element.
fifth_element = media.Movie(
                            "The Fifth Element",
                            "Korben Dallas (Willis), a taxicab driver and former special forces major,"
                            "after a young woman (Jovovich) falls into his cab. Dallas joins forces"
                            "with her to recover four mystical stones essential for the defence of"
                            "Earth against an impending attack (Wikipedia).",
                            "http://www.gstatic.com/tv/thumb/movieposters/19352/p19352_p_v8_af.jpg",  # noqa
                            "https://www.youtube.com/watch?time_continue=1&v=7-9mTiBawSM")  # noqa

# This the instance of the movie Star Wars.
star_wars = media.Movie(
                        "Star Wars",
                        "Thirty years after the defeat of the Galactic Empire, the galaxy faces a"
                        "new threat from the evil Kylo Ren (Adam Driver) and the"
                        "First Order (Wikipedia).",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQZKZtrlY3dnzsjBIGKR_b1QhkgZfM4-FIcH61uHnLQRR3WpNhk",  # noqa
                        "https://www.youtube.com/watch?time_continue=3&v=Hyc84zvhbQU")  # noqa

# This the instance of the movie Dark Knight.
dark_knight = media.Movie(
                          "Dark Knight",
                          "Bruce Wayne/Batman (Bale), James Gordon (Oldman) and"
                          "Harvey Dent (Eckhart) form an alliance to dismantle organised crime in"
                          "Gotham City, but are menaced by a criminal mastermind known as the Joker"
                          "who seeks to undermine Batman's influence and create chaos (Wikipedia).",
                          "http://host.trivialbeing.org/up/tdk-apr28-new-poster-posterexclusivoomelete6.jpg",  # noqa
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")  # noqa

# Here, movies is a list aka array.
movies = [big_hero, amelie, zootopia, fifth_element, star_wars, dark_knight]
# Fresh_tomatoes file will take in a list
# of movies to display in a webpage using the open_movies_page function.
fresh_tomatoes.open_movies_page(movies)
