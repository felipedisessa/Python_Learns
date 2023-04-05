class item:
    def __init__(self,name,description,price):
        self.name = name
        self.description = description,
        self.price = price
    def viewfulldescription(self):
        print(f"{mp3.name}")

class mp3(item):
    def __init__(self,artist,duration):
        self.artist = artist
        self.duration = duration
    def play(self):
        print("A musica iniciou")
    def download(self):
        print("A musica esta sendo baixad")

class dvd(item):
    def __init__(self,certificate,duration,actors):
        self.certificate = certificate
        self.duration = duration
        self.actors = actors
    def viewtrailer(self):
        print("O trailer será executado")

class book(item):
    def __init__(self,author, numberofpages, genre):
        self.author = author
        self.numberofpages = numberofpages
        self.genre = genre
    def previewcontent(self):
        print("Veja uma demonstração")

musica1 = mp3("Seila","1min")
musica1.name = "abc"
musica1.description = "nenhuma"
musica1.price = "R$ 100"
musica2 = mp3("Seila2","5min")
musica2.name = "Def"
musica2.descrpition = "Nenhuma"
musica2.price = "R$ 50"

dvd1 = dvd("123","2min","flavio")
dvd1.name = "dvd 00"
dvd1.description = "nenhuma"
dvd1.price = "R$ 10"
dvd2 = dvd("456","5min","paulo")
dvd2.name = "dvd 11"
dvd2.description = "nenhuma"
dvd2.price = "R$ 20"

book1 = book("carlos","10 pg","terror")
book1.name = "book ab"
book1.description = "nenhuma"
book1.price = "r$ 170"
book2 = book("lima","70 pg","comedia")
book2.name = "book cd"
book2.description = "nenhuma"
book2.price = "r$ 25"


