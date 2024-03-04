import json
import os

def save_emp():
    with open("employee.json","w")as file:
        json.dump(employee_data,file,indent=4)
def load_emp():
    global employee_data
    if os.path.exists("employee.json"):
        with open("employee.json","r+")as file:
            employee_data=json.load(file)
            
employee_data = {"count":0,"emp_list":[]}

def add_data():
    id = (input("enter your id :"))
    name = input("enter your name :")
    age = int(input("enter your age :"))
    phone_number = int(input("enter your phone number :"))
    experience = int(input("enter your experience :"))
    grade = input("enter your grade :")
    
    employee_data["count"]+=1
    employee_data["emp_list"].append({"id":id,"name":name,"age":age,"number":phone_number,"experience":experience,"grade":grade})
    
    save_emp()

    print("added successfully")
    
def get_display():
    print(employee_data)
    

def get_data():

    search_data = input("enter the id to search :")
  
          
    for employee in employee_data["emp_list"]:
        if employee["id"]==search_data:
            for key , value in employee.items():
                print(key,value)

# def add_update():
#    dddd
    
    
    
while True:
    load_emp()
    print("1. create employ")
    print("2. display")
    print("3. search ")
    print("4. update")
    print("5. exit")
    inputs = int(input("enter your choice :"))
        
    if inputs == 1:
        add_data()
    elif inputs == 2:
        get_display()
    elif inputs == 3:
        get_data()
    elif inputs == 4:
        add_update()
    elif inputs == 5:
        break
    else:
        print("sorry... something is wrong ")

