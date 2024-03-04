class movie:
    def __init__(self,title,director,genre,release_year):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year
        
    def display_info(self):
        print(f"title:{self.title}")
        print(f"director:{self.director}")
        print(f"genre:{self.genre}")
        print(f"release_year:{self.release_year}")  
    
    
movie1 = movie(title="inception",director="christopher",genre="sci-fi",release_year=2010) 
print(f"movie title:{movie1.title}")
print(f"director:{movie1.director}")  
movie1.display_info() 