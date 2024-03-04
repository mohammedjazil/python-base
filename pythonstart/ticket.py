ticket = int(input("enter your age :"))

if ticket <=3 :
    print("free")
elif 3 <=ticket <=12:
    print("10$")
elif 13 <=ticket <=18:
    print("15$")
elif ticket >=19:
    print("20$")
    
else:
    print("smothing wrong")