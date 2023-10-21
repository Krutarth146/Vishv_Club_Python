# Membership Operator   in,   not in

# list1 = [10,20,30,40,50,60]

# num = int(input())

# for i in range(len(list1)):
#     if list1[i] == num:
#         print(f"Element is Found at {i} index")
#         break
# else:
#     print('Not Found')


list2 = [i for i in range(1,101)]

print(list2)


if 96 in list2:
    print(True)   # True


del list2[5:]
print(list2)   # [1,2,3,4,5]

# list2.append("Aman")
# list2.append([10,20,30,40])

# print(list2)   # [1, 2, 3, 4, 5, 'Aman', [10, 20, 30, 40]]

list2.extend("Aman")
list2.extend([10,20,30,40,[50]])
list2.extend((34,10))
list2.extend((35,))
# list2.extend(34)   # int object is not iterable

print(list2)   # [1, 2, 3, 4, 5, 'A', 'm', 'a', 'n', 10, 20, 30, 40]


list2.insert(2,'Aman')
print(list2)   # [1, 2, 'Aman', 3, 4, 5, 'A', 'm', 'a', 'n', 10, 20, 30, 40, [50], 34, 10, 35]

list2[2] = "Manoj"
print(list2)   # [1, 2, 'Manoj', 3, 4, 5, 'A', 'm', 'a', 'n', 10, 20, 30, 40, [50], 34, 10, 35]

list2.insert(-1,100)
print(list2)   # [1, 2, 'Manoj', 3, 4, 5, 'A', 'm', 'a', 'n', 10, 20, 30, 40, [50], 34, 10, 100, 35]

print(len(list2))  # 19

list2.insert(19,200)

print(list2)   # [1, 2, 'Manoj', 3, 4, 5, 'A', 'm', 'a', 'n', 10, 20, 30, 40, [50], 34, 10, 100, 35, 200]


# int a[5]
# int a[5] = {10,20,30,40,50}
# int a[] = {10,20,30,40,50};
# int a[5] = {10,20,30,40,50};
# int a[5] = {10,20};
# int a[2] = {10,20,33,33};


# #define SIZE 10  # Macro
# int c[10];

# main()
# {
#     int b[SIZE];
#     c[1] = c[0] + 10;
# }

list1 = [10,20,30,40,50,60]
# tra = [20,30,40,50,60,60]



for i in range(len(list1)-1):
    temp = list1[i]
    list1[i] = list1[i+1]
    list1[i+1] = temp
    # list1[i], list1[i+1] = list1[i+1] , list1[i]

print(list1)

x = list1.pop()
print(list1, x)

x = list1.pop(2)
print(list1, x)  

list1.remove(30)

print(list1)


list1 = [10,20,30]

list2 = list1      # Deep Copy
list3 = list1.copy()  # Shallow Copy
list4 = list(list1)   # Shallow Copy


list1.append(900)
list2.append(9001)
print(list1, list2,list3,list4)

# --------------------------------------------------------

# String is Immutable (Unchangeble)

str1 = "Vishv is good good good Boy123."

# str1 = str1.replace('good', 'Bad', 2)

print(str1)   # Vishv is Bad Boy123.

list1 = str1.split(' ')
print(list1)

flag = 0
for i in range(len(list1)):
    if list1[i] == 'good':
        flag+=1
    if flag == 2:
        list1[i] = 'Bad'
print(list1)

str1 = ' '.join(list1)
print(str1)   # Vishv is good Bad good Boy123.


print(str1.partition(' '))   # ('Vishv', ' ', 'is good Bad good Boy123.')
print(str1.rpartition(' '))   # ('Vishv is good Bad good', ' ', 'Boy123.')
print(str1.split(' '))   # ['Vishv', 'is', 'good', 'Bad', 'good', 'Boy123.']


table = str1.maketrans('gd','jk','o')
print(table)   # {103: 98}


str1 = str1.translate(table)



print(str1)  # Vishv is bd Bad bd By123.


str1 = str1[::-1]
print(str1)

print(str1.rjust(55))

print(str1.find("z"))  # -1
# print(str1.index("z")) # Error


# list1 = [i for i in input().strip().split('_')]
# list1 = [i for i in input().strip().split(' ')]
# print(list1)   # ['Aman', '10', '[10,20,30]', "{'Ashok'", ':', '[10,20]}']


# o/p 

# Aman is String
# 10 is int
# [10,20,30] is list
# Ashok is Dict Key
# [10,20] is Dict Value


