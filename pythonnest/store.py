import os

def clear():
    os.system('clear')




store =[]

def addstr():
    clear()
    name=input("enter the product :")
    price=int(input("enter the price $ :"))
    quantity= int(input("enter quantity : "))
    
    prodt ={
        "name":name,
        "price":price,
        "quantity":quantity
    }
    store.append(prodt)
    clear()
    print(f"{name}added successfuly ")

def displaystr():
    clear()
    for i in store:
        print(f"name:{ i ['name']},price:{i['price']},quantity:{i['quantity']}")

        
def searchstr():
    clear()
    search_name = input("enter the product :")
    for i in store:
        if i['name']== search_name:
             print(f"name:{ i ['name']},price:{i['price']},quantity:{i['quantity']}")
        else:
            print("not found")
            

def updatestr():
    clear()
    name=input("enter the name :")
    upadtes = int(input("enter the quantity :"))
    for i in store:
        if i ['name']== name:
            i['quantity']=upadtes
            print(f"name:{ i ['name']},price:{i['price']},quantity:{i['quantity']}")
            
        
    
    
def rmstr():
    clear()
    search_del = input("product to delete:")
    for i in store:
        if i['name']== search_del:
            store.remove(i)
            clear()
            print(f"delete {i['name']} successfuly")
        else:
            print("not found")
          
def main():
    
    while True:
        print("enter 1 to add :")
        print("enter 2 to display :")
        print("enter 3 to search :")
        print("enter 4 to update :")
        print("enter 5 to remove :")
        print("enter 6 to exit :")
        value =(input("enter a option :"))
    
        if value=='1':
            addstr()
            
        elif value=='2':
            displaystr()
        
        elif value =='3':
            searchstr()
            
            
        elif value == '4':
            updatestr()
            
        elif value == '5':
            rmstr()
            
        elif value == '6':
            print("see you again !")
            break
        
        else:
            print("smothing error ! . pls try again")
        
if __name__ == "__main__":
    main()
clear()
        