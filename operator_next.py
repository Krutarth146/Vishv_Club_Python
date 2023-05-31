# Task: 
x = 78
print(~x)   # -79

y = -34
print(~y)   # 33   ----> 2's Complement, 1's Complement

# Logical Operators   and, or, not

print(23 and 89)   # 89
print(23 or 89)   # 23

# age = int(input())

# if age >= 18: 
#     print("You are Eligible for Voting.")
# elif age < 18:
#     print(f"You are Not Eligible for Voting, You need {18-age} more years.")
# else:
#     print("ENter Valid AGe")


# x = 80
# y = 78
# w = 56
# print()
# print(x,y,w,sep='\t')   # 80      78      56


if 0 != False:
    print(True)
else:
    print(False)

list1 = [10,20,30]
list2 = [10,30,20]

if not list1.sort() == list2.sort():
    pass
else:
    print("same")


num1 = 89
num2 = 67

if num1 < num2: print("num2 is Max")
else: print('Num1 is Max')


num1 = 670
num2 = 78
num3 = 560

if num2 < num1:
    if num3 < num1:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

# Comparison Operator / Relational ---> < > <= >= == !=

print(num1 if num1 > num2 else num2)

# 3 Variables


# Loops  ---> 1. Entry Control Loops ----> 1. while  2. for


num = 25  # start position

while num <= 100:   # Condition  (End Position)
    
    if num % 5 == 0 or num % 7 == 0 and num % 10 == 0:
        print(num, end=' ')
    
    num += 1   # Flow (Incre / Decre)

# 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100


x = 10
y = 10
# x += 20
print(id(x))   # 3190693102096
print(id(y))   # 3190693102096

# Identity O/p   ---> is , is not
if x == y:
    print("x == y")

if x is y:
    print("x is y")


list1 = [10,20,30,40]
list2 = [10,20,30,40]

print(id(list1))   # 2125429656192
print(id(list2))   # 2125425420864

if list1 == list2:
    print("list1 == list2")   # list1 == list2

if list1 is list2:
    print("list1 is list2")
else:
    print("list1 is not list2")


# Membership o/p   in , not in

list1 = [10,20,30,40,50]

need = int(input("Enter a Number: "))


# for(i=0; list1[i]!= need;i++)
# Linear Search
for i in list1:
    if i == need:
        print("Element is Found")
        break
else:
    print("Not Found")

print("Ele is found") if need in list1 else print("Not Found")
