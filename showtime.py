class Video():
    def __init__(self,video_title,video_duration):
        self.title = video_title
        self.duration = video_duration

class Movie(Video):
    def __init__(self,movie_title,movie_duration,movie_poster,movie_trailer):
        Video.__init__(self,movie_title,movie_duration)
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
    
