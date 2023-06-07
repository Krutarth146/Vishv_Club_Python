# List ---> Ordered, Mutable (Changeble), Allow Duplicates

list1 = []
print(type(list1))   # <class 'list'>

list1 = [10,10,10,20,10, 90.89, 'g', "scsbhcs", True, 90+8j, [{10,20,10,10,30,90}]]

print(list1)  # [10, 10, 10, 20, 10, 90.89, 'g', 'scsbhcs', True, (90+8j), [{10, 20, 90, 30}]]

print(id(list1))   # 2617595251328
print(len(list1))  # 11 (Length starts from 1, Index starts from 0)
print(list1.__sizeof__())  # 128


l1 = [10,20,30,40,50,60,70,10,20]


# Indexing
print(l1[0])  # 10
print(l1[-9])  # 10
print(l1[-1])  # 20
print(l1[4],l1[-4])  # 50 60

# Slicing

# print(l1[start:End(n-1):step(n-1)])
l1 = [10,20,30,40,50,60,70,10,20]

print(l1[1:4])  # [20, 30, 40]
print(l1[4:5])  # [50]
print(l1[5:1])  # []
print(l1[5:])  # [60,70,10,20]
print(l1[:3])  # [10,20,30]
print(l1[:])  # [10,20,30,40,50,60,70,10,20]
print(l1[-7:-1])  # [30, 40, 50, 60, 70, 10]
print(l1[-1:-7])  # []  
print(type(l1[4:5]))  # <class 'list'>


