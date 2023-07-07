tup1 = (10,20,30,[10,20,],(10,20,(10,20)), {10,101,10}, {'Name' : "Royal", 'Address' : "Gnr"})

print(tup1)   # (10, 20, 30, [10, 20], (10, 20, (10, 20)), {10, 101}, {'Name': 'Royal', 'Address': 'Gnr'})

# Tuple : Ordered (Indexed), Allow Duplicates, Immutable (Not Changeble)

print(len(tup1))  # 7
print(tup1.__sizeof__())  # 80

tup2 = (10,20,30,40)
print(sum(tup2))  # 100
print(min(tup2))  # 10
print(max(tup2))  # 40
print(max([10,20]))  # 20

list1 = [10,20,30,40,50,0]

print(min(list1))  # 10
print(all(list1))  # False
print(any(list1))  # True


# Polymorphism

# Poly - Many
# Morph - Forms Ex. Right - left, right - wrong -----> len, min, max, sum

tup2 = ((10,20,), (10,90,89), (11,67,84,{'Name' : "Manoj", 'address' : {"state" : "Guj", "City" : "Ahm", "House" : [90,45,78]}}))

print(tup2[2][-1]["address"]['House'][-2])  # 45


tup3 = (20,90,89.21,43,9,43,21,546,78)
print(tup3[-2])  # 89.21
print(tup3[1:2:-1])  # ()
print(tup3[-1:-4])  # ()
print(tup3[-3:4:2])  # ()

tup3 = (20,90,89.21,43,9,43,21,546,78)

print(tup3.count(43))  # 2
print(tup3.index(43,4))  # 5


for i in tup3:
    print(i)

for i in tup3[::-1]:
    print(i)

for k in reversed(tup3):
    print(k)

for l in range(3,-1,-1):
    print(tup3[l])

for l in range(len(tup3) - 6,-1,-1):
    print(tup3[l])


tup5 = (10,90,80,10,10,10,10)


l1 = []

for i in tup5:
    if i not in l1 and tup5.count(i) == 1:
        l1.append(i)

print(l1)  # [90, 80]

# -----------------------
l2 = []
for k in range(len(tup5)-1):
    for ayush in range(k+1,len(tup5)):
        if tup5[k] != tup5[ayush]:
            if tup5[k] not in l2:
                l2.append(tup5[k])

print(l2)  # [10,90,80]

print()
print()
print()
# -----------------------
l2 = []
tup5 = (10,90,80,10,10,10,10)
tup5 = list(tup5)
for k in tup5:
    if tup5.count(k) > 1:
        print(tup5)
        for i in range(tup5.count(k)):
            tup5.remove(k)

print(tup5)  # [10,90,80]

tup5 = (10,90,80,10,10,10,10)
tup5 = set(tup5)
print(tup5)  # {80, 10, 90}  # Don't Allow Duplicates, Unordered


# ---------------------------


l1 = [0,1,1,1,0,1,0,0,1,1,0,1,0]

