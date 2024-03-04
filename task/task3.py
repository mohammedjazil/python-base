import os

airport =[]

def clear():
    os.system('clear')
    

def add_detials():
    clear()
    flight_num=int(input("enter the flight number :"))
    destination=(input("enter the destination :"))
    departure = int(input("enter departure time : "))
    
    flight ={
        "flight_num":flight_num,
        "destination":destination,
        "departure":departure,
        "passengers":[]
    }
    airport.append(flight)
    print(f"flight {flight_num} added successfuly ")
    
    
def add_passenger():
    clear()
    flight_num = int(input("enter flight number to add passengers :"))
    for flight in airport:
        if flight['flight_num'] == flight_num:
            passenger_name = input("enter passenger name :")
            flight['passengers'].append(passenger_name)
            print(f"passenger {passenger_name} added to flight {flight_num}")
            break
    else:
        print("not found")
def displaydetials():
    clear()
    if not airport:
        print("no flight")
    else:
        for i in airport:
            print(f"flight number:{ i ['flight_num']},destination:{i['destination']},departure:{i['departure']}")

          
def main():
    
    while True:
        print("enter 1 to add :")
        print("enter 2 to addin passengers :")
        print("enter 3 to display:")
        print("enter 4 to exit :")
        value =(input("enter a option (1-4):"))
    
        if value=='1':
            add_detials()
            
        elif value=='2':
            add_passenger()
        
        elif value =='3':
            displaydetials()
            
        elif value == '4':
            print("see you again !")
            break
        
        else:
            print("smothing error ! . pls try again")
        
if __name__ == "__main__":
    main()