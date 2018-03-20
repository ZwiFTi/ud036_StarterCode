import media
import fresh_tomatoes

''' this module creates instances of movies and passes
    them in a list to other modules '''

s1 = media.Movie("Sharknado",
                 "https://upload.wikimedia.org/"
                 "wikipedia/en/9/93/Sharknado_poster.jpg",
                 "https://www.youtube.com/watch?v=M-pXDoe5a0E")

s2 = media.Movie("Sharknado 2",
                 "https://upload.wikimedia.org/"
                 "wikipedia/en/3/35/Sharknado_2_poster.jpg",
                 "https://www.youtube.com/watch?v=U3-7-kf6tVc")

s3 = media.Movie("Sharknado 3",
                 "https://upload.wikimedia.org/"
                 "wikipedia/en/5/5e/Sharkando_3_poster.jpg",
                 "https://www.youtube.com/watch?v=gP2j5lyKwKM")

s4 = media.Movie("Sharknado 4",
                 "https://upload.wikimedia.org/"
                 "wikipedia/en/4/4e/Sharkando_4_poster.jpg",
                 "https://www.youtube.com/watch?v=YwIsEPNHGsc")

s5 = media.Movie("Sharknado 5",
                 "https://images-na.ssl-images-amazon.com/images/"
                 "M/MV5BMjQ3Mzk5NzAwNV5BMl5BanBnXkFtZTgwNDkwOTc3MjI"
                 "@._V1_UX182_CR0,0,182,268_AL_.jpg",
                 "https://www.youtube.com/watch?v=hbRroXtmvOU")

s6 = media.Movie("Inception",
                 "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                 "Inception_%282010%29_theatrical_poster.jpg",
                 "https://www.youtube.com/watch?v=YoHD9XEInc0")

movies = [s1, s2, s3, s4, s5, s6]

if __name__ == "__main__":
    # Open website in browser, fill in with movies
    fresh_tomatoes.open_movies_page(movies)
