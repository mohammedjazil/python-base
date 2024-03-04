text = "apple,banana,orange"

fruits = text.split(",")
print(fruits)


text = "apple,banana,orange,mango"

fruits = text.split(",",maxsplit=2)
print(fruits)

