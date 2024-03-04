# size = 5

# for i in range(size):
#     for j in range(size):
#         print("*",end="")
#     print()



# size = 5

# for i in range(size):
#     for j in range(i+1):
#         print("*",end="")
#     print()


for i in range(1,6):
    for j in range(1,11):
        result =i *j
        print(f"{i}x{j}={result}",end="\t")
    print()