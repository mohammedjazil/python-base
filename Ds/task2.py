def main ():
    data = input("enter a string :")
    
    print("capitaized string :",data.upper())
    
    
    digit = int(input("enter the width for centering :"))
    center = data.center(digit)
    print("centered string :",center)
     
      
    sub = input("enter a substring to count :")
    count = data.count(sub)
    print(f"count of '{sub}' :{count}")
    
    
    suf = input("enter a suffix to check at the end :")
    fix= data.endswith(suf)
    print(f"ends with '{suf}' :{fix}")
    
    fi = input("enter a substring to find :")
    find = data.find(fi)
    print(f"index of '{fi}':{find}")
    
    
    name = input("enter your name :")
    age = int(input("enter your age :"))
    format = "my name is {}, i am {} years old.".format(name,age)
    print("fomatted string :",format)
    

if __name__ == "__main__":
    main()