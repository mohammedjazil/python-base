class book:
    def __init__(self,title,auther,genre,publication_year):
        self.title = title
        self.auther = auther
        self.genre =genre
        self.publication_year = publication_year
        
    def display_info(self):
        print(f"title: {self.title} ")
        print(f"auther:{self.auther}")
        print(f"genre:{self.genre}")
        print(f"pulication_year:{self.publication_year}")
        
title = input("enter the title :")
auther = input("enter auther name :")
genre = input("enter the genre :")
year = int(input("enter the year :"))

book1 =book(title="king",auther="jazil",genre="thriller",publication_year=2023)

book1.display_info()