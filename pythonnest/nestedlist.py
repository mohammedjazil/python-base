# nested_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
    
# ]

# print(nested_list[0][1])
# print(nested_list[2][0])


# students = [
#     ["alice",90,88,94],
#     ["bob",75,82,80],
#     ["charlie",88,95,78]    
# ]

# for student in students:
#     print(f"{student[0]}'s grades:{student[1:]}")
    
    
nested_list =[
    [1,2,3],
    [4,5,6],
    [7,8,[9,10]],
    [11,[12,13],14]
]

print(nested_list[1][0])
print(nested_list[2][2][1])
print(nested_list[2][2][0])
print(nested_list[3][1][0])
nested_list[0][0]= 100


newlist = [20,30,40]
nested_list.append(newlist)
print(nested_list)