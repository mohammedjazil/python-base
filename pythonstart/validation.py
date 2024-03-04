# flag =0
# while flag == 0:
#     try:
#         num_1 = int(input("enter a value:"))
#         print(num_1)
#         flag = 1
#     except:
#         print("enter numbes only")

flag=0
while flag==0:
    try:
        count=0
        while count<3:
             password = int(input("enter a name:"))
             if password==123:
                 print("success")
                 flag=1
             else:
                print("wrong password")
    except:
        print("try again")