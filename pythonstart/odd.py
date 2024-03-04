while True:
    try:
        num = int(input("enter a number :"))
    
        if num %2==0:
            print("even")
        else:
            print("odd")
            break
    except:
        print("error")
        