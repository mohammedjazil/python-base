class student:
    def __init__(self,name,mark):
        self.name = name
        self.name = mark
        
    
    def getvalue(self):
        self.name = input("enter your name :")
        self.age = int(input("enter yr age :"))
        print(self.name,self.age)
        

class parent(student):
    def printp(self):
        print("i am parent")
        
class teacher(parent):
    def printt(self):
        print("i am teacher ")
        
        
t1 = teacher('','')
t1.getvalue()
t1.printp()
t1.printt()