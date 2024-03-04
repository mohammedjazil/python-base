book = {}

while True:
    print("1. add a book ")
    print("2. display all book titles")
    print("3. display details of a book")
    print("4. remove a book")
    print("5. display all book details ")
    print("6. clear the dictionary")
    print("7. create a copy of the dictionary  ")
    print("8. display items and keys")
    print("9. pop the last inserted item")
    print("10. set default details for a title")
    print("11. update details")
    print("12. exit")
    value = input("enter your choice (1-12):")
    
    if value == "1":
        name = input("enter name of book :")
        details = input("enter details :")
        book[name] = details
        print(book)
    
    elif value == '2':
        print(book)
        
        
    elif value == "3":
        name = input("enter to add a name :")
        book_details = book.get(name)
        print(book_details)
        
        
    elif value == "4":
        name = input("enter to remove name :")
        book.pop(name)
        
        
    elif value == "5":
        book_details = book.values()
        print(book_details)


    elif value == "6":
        book.clear()
        print(book)
    
    elif value == "7":
        copy = book.copy()
        print(copy)
        
    elif value == "8":
        for titlt,details in book.items():
            print(f"title : {titlt}, details : {details}")
        else:
            print("not found")
                

    elif value == "9":
        book.popitem()
        print(book)
        
    elif value == "10":
        name = input("enter book name :")
        details = input("enter details :")
        default_details = book.setdefault(name,details)
        print(default_details)
        
    elif value == "11":
        name = input("enter book name :")
        details = input("enter details :")
        book_dict = {name:details}
        book.update(book_dict)
    
    elif value == "12":
        break
    
    else:
        print("invalid")