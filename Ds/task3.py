person = []

while True:
    print("1. add a name ")
    print("2. remove name ")
    print("3. append name ")
    print("4. insert name ")
    print("5. pop name ")
    print("6. reverse order")
    print("7. extend list ")
    print("8. get numbers and sort ")
    print("0. exit ")
    value = input("enter your choice (0-8):")
        
        
    if value == "1":
        name = input("enter your name :")
        person.append(name)
        print(person)
    
    elif value == '2':
        remov = input("enter to remove a name :")
        person.remove(remov)
        print(person)
        
    elif value == "3":
        appen = input("enter to add a name :")
        person.append(appen)
        print(person)
    
    elif value == "4":
        inser = input("enter to insert a name :")
        pos = int(input("enter position :"))
        person.insert(pos,inser)
        print(person)
        
    elif value == "5":
        pop = input("enter to pop a name :")
        pos = int(input("enter position :"))


    elif value == "6":
        person.reverse()
        print(person)
    
    elif value == "7":
        back_end = input("enter to extent :")
        person.extend(back_end)
        print(person)
    
    elif value == "8":
        person.sort()
        print(person)
        
    elif value == "0":
        break
    