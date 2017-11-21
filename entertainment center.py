import fresh_tomatoes
import media

#define instances
toy_story=media.Movie("Toy Story",
                      "Toys in real life",
                      "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

dark_knight=media.Movie("The Dark Knight",
                        "Featuring the DC Comics character Batman",
                        "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

hunger_games=media.Movie("The Hunger Games",
                         "The Hunger Games is a trilogy of young adult dystopian novels",
                         "https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg",
                         "https://www.youtube.com/watch?v=mfmrPu43DF8")

face_off=media.Movie("Face Off",
                     "Face/Off is a 1997 American science fiction action film",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcRIGCQjNfR3eYrO0DJCLMOpQpuz22o3PLvvvsxeQ2SHlNUFvy0m",
                     "https://www.youtube.com/watch?v=95VvTW1FvS8")

gone_girl=media.Movie("Gone Girl",
                      "Gone Girl is a 2014 American psychological thriller film",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcTwcWs6CK22NdvXZH0CbigLxoV-N3GIJypphImFYYv1vG_VKXTQ",
                      "https://www.youtube.com/watch?v=2-_-1nJf8Vg")

pursuit_of_happyness=media.Movie("Pursuit of Happyness",
                                 "Life is a struggle for single father Chris Gardner (Will Smith)",
                                 "http://www.gstatic.com/tv/thumb/movieposters/162523/p162523_p_v8_ad.jpg",
                                 "https://www.youtube.com/watch?v=89Kq8SDyvfg")

inside_out=media.Movie("Inside Out",
                       "Riley's emotions -- led by Joy -- try to guide her through her life",
                       "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                       "https://www.youtube.com/watch?v=seMwpP0yeu4")

split=media.Movie("Split",
                  "A man with 23 personalities",
                  "https://fsmedia.imgix.net/fe/d8/c9/44/5e54/47d9/a248/032a9018b4f2/james-mcavoy-in-split.jpeg",
                  "https://www.youtube.com/watch?v=84TouqfIsiI")

shawshank_redemption=media.Movie("Shawshank Redemption",
                      "The Shawshank Redemption is a 1994 American drama film.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                      "https://www.youtube.com/watch?v=6hB3S9bIaco")

#movies list to store instances
movies=[toy_story,
        dark_knight,
        hunger_games,
        face_off,
        gone_girl,
        pursuit_of_happyness,
        inside_out,
        split,
        shawshank_redemption]

#insert movies as parameter
fresh_tomatoes.open_movies_page(movies)
