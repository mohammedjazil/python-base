import json
import os


employee_data = {"count":0,"emp_list":[]}

def add_data():
    name = input("enter your name :")
    age = input("enter your age :")
    employee_data["count"]+=1
    employee_data["emp_list"].append({"name":name,"age":age})
    
    with open("employee.json","w")as file:
        json.dump(employee_data,file,indent=4)
    
    print("added successfuly")
    
def get_data():

    search_data = input("enter the name to search :")
    if os.path.exists("employee.json"):
        with open("employee.json","r+")as file:
            employee_data=json.load(file)
            
    for employee in employee_data["emp_list"]:
        if employee["name"]==search_data:
            for key , value in employee.items():
                print(key,value)
    
while True:
    inputs = int(input("enter your choice :"))
        
    if inputs == 1:
        add_data()
    elif inputs == 2:
        get_data()
