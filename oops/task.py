class Product:
    def __init__(self,add,display,delet):
        self.add = add
        self.display = display
        self.delet = delet

    def display_info(self):
        print(f"{self.add} {self.display} {self.delet}")
    
              
class grocery_store(product):
    def _init_(self):
        self.product =[]
        
    def add_product(self,product):
        self.produts.append(book)
        print(f"Product {'product.add'} added to store")

    
    def remove_product(self,product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product {'book.add'} removed from ")
            

 
        name=input("enter the product :")
        price=int(input("enter the price $ :"))
        quantity= int(input("enter quantity : "))
        
        pro ={
            "name":name,
            "price":price,
            "quantity":quantity
        }
        product.append(pro)
        print(f"{name}added successfuly ")





def main():
     
    while True:
        
            
        print("enter 1 to add :")
        print("enter 2 to display :")
        print("enter 3 to delete :")
        value =(input("enter a option :"))
            
        if value=='1':
                addp()
                        
        else:
                print("smothing error ! . pls try again")

if __name__ == "__main__":
    main()

r1= grocery_store('','')
r1.addp()
