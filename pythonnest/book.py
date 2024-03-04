books = []

def addbook():
    head =input("enter tile :")
    auther=input("enter auther name :")
    genre= input("genre :")
    
    book1 ={
        "title":head,
        "auther":auther,
        "genre":genre
    }
    books.append(book1)
    print(f"book {head} added")
    
def displaybook():
    for book1 in books:
        print(f"title: {book1['title']}, auther :{book1['auther']},genre: {book1['genre']}")
        
def searchbook():
    search_name = input("enter book name:")

    for book1 in books:
        if book1['name'] == search_name:
            print(f"title: {book1['title']}, auther :{book1['auther']},genre: {book1['genre']}")
        else:
            print("not found")

while True:
    print("enter 1 to add :")
    print("enter 2 to display :")
    print("enter 3 to search :")
    print("enter 4 to exit :")
    value = input("enter the key here :")
    
    if value=='1':
        addbook()
        
    elif value=='2':
        displaybook()
        
    elif value=='3':
        searchbook()
        
    elif value =='4':
        print("have a nice daay")
        break
        
    else:
        print("try again . smothing wrrong")