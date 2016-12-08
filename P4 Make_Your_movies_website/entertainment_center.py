import media
import fresh_tomatoes

silence_of_the_lambs = media.Movie("silence of the lambs",
                                   "findind a serial killer",
                                   "http://t3.gstatic.com/images?q=tbn:ANd9GcRCZLkDY7eSQu1ndh7m9JQkvzXVvW9VrBzT_anh5Lf4kT84-4ev",
                                   "https://youtu.be/lQKs169Sl0I")
murari = media.Movie("murari",
                     "The curse of ancestors",
                     "https://upload.wikimedia.org/wikipedia/en/6/6a/Murari_Audio.jpg",
                     "https://youtu.be/2cmWLJyTKjc")

departed = media.Movie("departed",
                       "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston",
                       "http://www.gstatic.com/tv/thumb/movieposters/162564/p162564_p_v8_ag.jpg",
                       "https://youtu.be/auYbpnEwBBg")

spider_man = media.Movie("spider man",
                         "A spider man helping people from troubles",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcQVzjsQN4VSZaWDXWYf1dCLQ6fU3ArTWTMh9fwmYcMke_RsOgP6",
                         "https://youtu.be/O7zvehDxttM")

yem_mayachesave = media.Movie("yem maya chesave",
                              "Not all the love stories are same",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Yemaaya.jpg/220px-Yemaaya.jpg",
                              "https://youtu.be/93dT9aZDQw8")

rockstar = media.Movie("Rockstar",
                       "Janardhan Jakhar chases his dreams of becoming a big Rock star, during which he falls in love with Heer",
                       "http://cdn.wallpapersafari.com/3/93/Kegwf0.jpg",
                       "https://youtu.be/RThZ5rupqcc")


movies =[silence_of_the_lambs,murari,departed,spider_man,yem_mayachesave,rockstar]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
