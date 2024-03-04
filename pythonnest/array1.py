employee =[]

def addemp():
    name =input("enter your name :")
    age = int(input("enter your age :"))
    job = input("enter your job postion :")
    
    
    empl={
        "name":name,
        "age":age,
        "job":job
    }
    employee.append(empl)
    print(f"employee {name} added successfuly")

def displayemp():
    for employ in employee:
        print(f"name: {employ['name']}, age :{employ['age']},job: {employ['job']}")
        
def searchemp():
    search_name = input("enter user name :")

    for employ in employee:
        if employ['name'] == search_name:
            print(f"name: {employ['name']}, age :{employ['age']},job: {employ['job']}")
        else:
            print("not found")
            
def delemp():
    search_del= input("enter name to delete :")
    for employ in employee:
        if employ['name'] == search_del:
            employee.remove(employ)
        else:
            print("not found")
        

while True:
    print("enter 1 to add")
    print("enter 2 to display")
    print("enter 3 to search")
    print("enter 4 to delete")
    value = input("enter the key here :")
    
    if value=='1':
        addemp()
        
    elif value=='2':
        displayemp()
        
    elif value=='3':
        searchemp()
    
    elif value=='4':
        delemp()
        
    elif value =='5':
        print("have a nice daay")
        break
        
    else:
        print("try again . smothing wrrong")