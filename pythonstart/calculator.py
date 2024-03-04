num_1=int(input("enter a number:"))
num_2=int(input("enter a number :"))

opern=(input("enter operation :"))

if opern == "+":
    print(num_1+num_2)

elif opern == "-":
    print(num_1-num_2)

elif opern == "*":
    print(num_1*num_2)

elif opern == "/":
    if num_2!=0:
        print(num_1/num_2)
        
else:
    print("somthing wrong")