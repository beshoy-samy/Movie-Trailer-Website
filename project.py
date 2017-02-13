import fresh_tomatoes as magician
import showtime

sing = showtime.Movie("Sing","1 hr 48 mins",
                            "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                            "https://www.youtube.com/watch?v=9qPgK_u4vX8")

hacksaw_ridge = showtime.Movie("Hacksaw Ridge","2 hrs 19 mins",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
                            "https://www.youtube.com/watch?v=sslCRVx7nPQ")

zootopia = showtime.Movie("Zootopia","1 hr 48 mins",
                            "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                            "https://www.youtube.com/watch?v=jWM0ct-OLsM")


movies = [sing,hacksaw_ridge,zootopia]

magician.open_movies_page(movies)
