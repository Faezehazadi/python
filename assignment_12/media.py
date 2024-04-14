
import pytube

class Media:
    def __init__(self,type,name,director,imdb_score,url,duration,actor):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.actor = actor 

def download(self):
    link = self.url
    fs = pytube.YouTube(link).streams.first()
    fs.download(output_path='./', filename = 'test.mp4')