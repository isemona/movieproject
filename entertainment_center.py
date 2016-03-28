import fresh_tomatoes
import media


big_hero = media.Movie("Big Hero 6",
                        "A story of a young robotics prodigy named Hiro Hamada who forms a superhero team to combat a masked villain.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",
                        "https://www.youtube.com/watch?v=z3biFxZIJOQ")#self is added by default

#print (toy_story.storyline)
#toy_story.show_trailer()

amelie = media.Movie("Amelie",
                        "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                        "http://cdn.miramax.com/media/assets/Amelie1.png",
                        "http://www.magiclanternfilmsociety.org/wp-content/uploads/2012/06/Amelie.jpg")

zootopia = media.Movie("Zootopia",
                        "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                        "http://vignette4.wikia.nocookie.net/disney/images/2/2f/Zootopia_Poster.jpg/revision/latest?cb=20151210185516",
                        "https://www.youtube.com/watch?v=bY73vFGhSVk")

fifth_element = media.Movie("The Fifth Element",
                        "Korben Dallas (Willis), a taxicab driver and former special forces major, after a young woman (Jovovich) falls into his cab. Dallas joins forces with her to recover four mystical stones essential for the defence of Earth against an impending attack.",
                        "http://www.gstatic.com/tv/thumb/movieposters/19352/p19352_p_v8_af.jpg",
                        "https://www.youtube.com/watch?time_continue=1&v=7-9mTiBawSM")


star_wars = media.Movie("Star Wars",
                        "Thirty years after the defeat of the Galactic Empire, the galaxy faces a new threat from the evil Kylo Ren (Adam Driver) and the First Order.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQZKZtrlY3dnzsjBIGKR_b1QhkgZfM4-FIcH61uHnLQRR3WpNhk",
                        "https://www.youtube.com/watch?time_continue=3&v=Hyc84zvhbQU")

dark_knight = media.Movie("Dark Knight",
                        "Bruce Wayne/Batman (Bale), James Gordon (Oldman) and Harvey Dent (Eckhart) form an alliance to dismantle organised crime in Gotham City, but are menaced by a criminal mastermind known as the Joker who seeks to undermine Batman's influence and create chaos.",
                        "http://host.trivialbeing.org/up/tdk-apr28-new-poster-posterexclusivoomelete6.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")


movies = [big_hero, amelie, zootopia, fifth_element, star_wars, dark_knight]
fresh_tomatoes.open_movies_page(movies)
