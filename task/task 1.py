import os

school =[]

def clear():
    os.system('clear')

def add_student():
    clear()
    name=input("enter the student name :")
    
    students ={
        "name":name,
        "status":None
    }
    school.append(students)
    print(f"{name} added successfuly")
    
    
def add_present():
    clear()
    name = input("enter student name :")
    
    flag = False
    for i in school:
        if i['name'] == name:
            i['status'] ='present'
            print(f"{name} marked as present")
            flag = True
            break
    
    if not flag:
        print(f"{name} not found")
        
def add_absent():
    clear()
    name = input("enter student name :")
    
    flag = False
    for i in school:
        if i['name'] == name:
            i['status'] ='absent'
            print(f"{name} marked as absent")
            flag = True
            break
    
    if not flag:
        print(f"{name} not found")

def display_student():
    clear()
    print("attendence status :")
    for i in school:
        status = i['status'] if i['status'] else 'not marked'
        print(f"{ i ['name']}:{status}")
        

def main():
    clear()
    while True:
        print("enter 1 to add name :")
        print("enter 2 to add present")
        print("enter 3 to add absent :")
        print("enter 4 to display  :")
        print("enter 5 to exit :")
        value =(input("enter a option (1-5):"))
    
        if value=='1':
            add_student()
            
        elif value=='2':
            add_present()

        elif value=='3':
            add_absent()
                 
        elif value=='4':
            display_student()
            
        elif value == '5':
            print("see you again !")
            break
        
        else:
            print("smothing error ! . pls try again")
        
if __name__ == "__main__":
    main()