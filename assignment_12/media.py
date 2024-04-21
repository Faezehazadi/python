
import pytube
video = []
class Media:
    def __init__(self,type,name,director,imdb_score,url,duration,actor):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.actor = actor 

def download():
    for obj in video:
        if obj.name == media_name:
            first_stream = YouTube(obj.url)


