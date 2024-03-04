import os
os.system("clear")

from add1 import *
from multi import *
from sub1 import *


num_1=int(input("enter the 1st number :"))
num_2=int(input("enter the 2nd number :"))

result= add(num_1,num_2)
result1= multiple(num_1,num_2)
result2= sub(num_1,num_2)
print(result,result1,result2)