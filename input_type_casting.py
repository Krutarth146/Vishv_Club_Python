# scanf("%d",&num);   in c

# num = input("Enter a Number: ")
# print("Number: ",num)
# # printf("%d",*p);
# print(id(num))   # 2654062195440
# print(type(num))   # <class 'str'>

# num1 = input("Enter Num1: ")  # 90 ---> str
# num2 = input("Enter Num2: ")  # 20 ---> str

# print(num1 + num2)   # 9020  # str + str (Concat)


# Datatypes and Typecasting

x = 67
print(type(x))   # <class 'int'>

y = 90.78
print(type(y))   # <class 'float'>

z = 'w'
print(type(z))  # <class 'str'>

d1 = "Vishv Raval"
print(type(d1))   # <class 'str'>

_1 = 90 + 67j    # 90 is Real Part, 67 is Imaginary Part
print(type(_1))  # <class 'complex'>

_2 = 34  # int

print(_1 + _2)   # (124+67j)  # complex

p = "True"
print(type(p))   # <class 'str'>
p = True
print(type(p))   # <class 'bool'>

K_1 = None
print(type(K_1))  # <class 'NoneType'>

l = 0
print(type(l))

if 0 == False:
    print(True)
else:
    print(False)

# Collections

hj = [10,20,30,10,90.89,"str1",90+8j, False, [[10,20],[(89,89)]], {'set1', 90}, {"Name" : "Krutarth", 'Roll' : 900}]
print(type(hj))   # <class 'list'>   # Ordered
 
tup1 = ()  # Imutable   # Ordered
print(type(tup1))  # <class 'tuple'>

dict1 = {}
print(type(dict1))  # <class 'dict'>  # Ordered

s1 = {10,20,((10,10,10), (20,30)),10,10}   # A set is a collection which is unordered, unchangeable*, and unindexed.
print(s1)   # {10, 20, (10, 10, 10)}
print(type(s1))  # <class 'set'>

dict2 = {"school" : "HBK", 90 : 89, 'address' : {"State" : "Gujarat", "city" : "Ahm"} }
print(dict2)   #  {'school': 'HBK', 90: 89, 'address': {'State': 'Gujarat', 'city': 'Ahm'}}
print(type(dict2))  # <class 'dict'>

# Typecasting ---> 1. Implicit Typecasting    2. Explicit Typecasting

x = 90     # Int
t = 56.89  # Float

print(x + t)  # 146.89   # Implicit Typecasting

b = True   # Bool  ---> 1
w = 78     # int    ----> 78

print(b+w)  # 78 + 1 = 79   # Implicit


d = bool(-78.32)   # Explicit 
q = 89
print(d + q)  # 90  # Implicit

v = "w"
# print(int(v))  # Error

print(ord(v))   # 119

print(chr(69))   # E

d = '89'
s = 78
print(int(d) + s)   # 167  # Explicit Typecasting

d = '78.89'
print(int(float(d)))  # 78

import math

print(math.ceil(78.89))   # 79
print(math.ceil(78.00001))   # 79
print(math.ceil(78.00000))   # 78

print(math.floor(78.89))   # 78
print(math.floor(78.9999))   # 78

print(round(78.89))  # 79
print(round(72.89,-1))  # 70.0
print(round(75.89,-2))  # 100.0


print(45 / 2)  # 22.5  (float)
print(46 / 2)  # 23.0  (float)

print(23//2)   # 11 (Floor Division)

print(-18 // 4)  # -5

# Calc

num1 = int(input("Enter Num1: ")) 
num2 = int(input("Enter Num2: "))

print(num1 + int(num2))   # 30

print(type(num2))  # str

#  Arithmetic O/p:    +  -  *  /  //  %  **

print(f"{num1} + {num2} = {num1 + num2}")   # 110
print(f"{num1} - {num2} = {num1 - num2}")   # 70


# H.w.

# Area 5 Programs (3.14 * r * r * h)

# Take days as Input from User and Find Total No. of Years, months and remaing Days
# 400 ---> 1 Year, 1 month, 5 remaining Days

# Seconds ---> Hour, Minuts, rem_seconds

# Ascii , Operator Precedence & Assoiciativity