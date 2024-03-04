my_dict ={}

new_data = {'name':'john','age':25,'city':'new york'}

my_dict.update(new_data)

print(my_dict)

my_dict_copy = my_dict.copy()

print(my_dict_copy)

my_dict.pop('age')
print(my_dict)


my_dict_copy.clear()
print(my_dict_copy)