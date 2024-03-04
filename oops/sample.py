class person:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
  
    def greet(self):
        print(f"hello,my name is {self.name}.")

person_1 = person(name="john",age=30)

print(f"person's name:{person_1.name}")
print(f"age:{person_1.age}")

person_1.greet()