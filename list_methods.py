# List ---> Allow's Duplicates, Ordered (Indexed), Mutable (Chnageble)

list1 = []
print(type(list1))  # <class 'list'>

l2 = [10,10,20,30,True,78+8j]
l3 = [10,10,20,30,True,78+8j]

print(len(l2))  # 6 ---> Length starts from 1 & Index starts from 0
print(l2.__sizeof__())  # 88
print(id(l2))  # 2317685892736
print(id(l3))  # 1686201224000

l3 = l2   # Deep Copy

x = 90
f = 90

print(id(x))  # 2911004658704
print(id(f))  # 2911004658704

if x is f:   # Identity O/p
    print("x is f")

if l2 is l3:
    print("l2 is l3")  # l2 is l3


vishv = l2    # Deep Copy  (phy Adhar Card == Digilocker)
manoj = l2.copy()   # Shallow COpy (phy Adhar card == xerox)

l2.append("Royal")

print(l2)     # [10, 10, 20, 30, True, (78+8j), 'Royal']
print(vishv)  # [10, 10, 20, 30, True, (78+8j), 'Royal']
print(manoj)  # [10, 10, 20, 30, True, (78+8j)]

vishv.append(5000)
print(l2)

l1 = [10,20,30,40]

l1+=[900,89,78,'str']

print(l1)  # [10, 20, 30, 40, 900, 89, 78, 'str']

l1.append("True")
print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True']

l1.extend("str1")
print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1']


temp = [89, 67, 8945]

l1.append(temp)
print(l1)    # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945]]

# l1.extend(temp)
# print(l1)    # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', 89, 67, 8945]

# l1.extend(4500) # int object is not Iterable Gives Error
l1.extend([4500])
print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 4500]


l1.insert(1, 7800)
print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 4500]

l1.insert(-1, 9000)
print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 9000, 4500]

l1[-1] = 789363 
print(l1)   # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 9000, 789363]

# del l1   delete whole l1



# Remove Elements

del l1[8:]
print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78]

print(l1.pop())  # 78
print(l1)   # [10, 7800, 20, 30, 40, 900, 89]

l1.pop(3)
print(l1)   # [10, 7800, 20, 40, 900, 89]

l1.remove(7800)
print(l1)   # [10, 20, 40, 900, 89]

# -------------------


# l1.sort()   # default ---> Increasing order
# print(l1)   # [10, 20, 40, 89, 900]

# l1.reverse()
# print(l1)   # [900, 89, 40, 20, 10]

l1.sort(reverse=True)
print(l1)   # [900, 89, 40, 20, 10]

# l1.clear() # Clear l1

print(l1.count(900))  # 1   # frequency
print(l1.index(900))  # 0   # Index (Position)


for i in l1:
    print(i)

for d in range(len(l1)):  # start - 0, end = 4
    print(l1[d],end=' ')   # 900 89 40 20 10