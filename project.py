import fresh_tomatoes as magician
import showtime

#create a movie object named sing
sing = showtime.Movie("Sing","1 hr 48 mins",
                            "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                            "https://www.youtube.com/watch?v=9qPgK_u4vX8")

hacksaw_ridge = showtime.Movie("Hacksaw Ridge","2 hrs 19 mins",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
                            "https://www.youtube.com/watch?v=sslCRVx7nPQ")

zootopia = showtime.Movie("Zootopia","1 hr 48 mins",
                            "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                            "https://www.youtube.com/watch?v=jWM0ct-OLsM")

#print(showtime.Movie.__doc__)

#creting list contains all the movies that have been created
movies = [sing,hacksaw_ridge,zootopia]
#calling method from magician creates the HTML page containing all the movies
magician.open_movies_page(movies)
