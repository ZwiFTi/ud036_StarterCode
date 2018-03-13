class Movie:
    """ This class provides a blueprint for
        creating instances of movies

        attributes:
        title: A movie title
        poster_image_url: Takes a url path of a image
        trailer_youtube_url: Takes a url path to a url video

        """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
