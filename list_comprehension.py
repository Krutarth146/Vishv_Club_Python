list1 = [10, 89 , 67, 45, 32, 21]
odd = []
for i in list1:
    if i % 2 != 0:
        odd.append(i)
print(odd)



res1 = [i for i in list1 if i % 2 != 0]
print(res1)


# -------------------------

div3 = [i for i in range(25,0,-1) if i % 3 == 0]
print(div3)  # [24, 21, 18, 15, 12, 9, 6, 3]


lst3 = [
    [10,20,30], 
    [40,50,60], 
    [80,90,67]
    ]

for i in lst3:
    for k in i:
        print(k)

print([k for i in lst3 for k in i if k % 10 == 0])


# ----------------------------------


l1 = [10, 89, 67, 56, 45]

# [(10,10), (10,89), (10,67)....]


for j in l1:  # j = 10
    for g in l1:  # g = 10 89 67 56 45
        print((j,g),end=' ')


print([(j,g) for j in l1 for g in l1])

# ------------------------


l3 = [10, 89, 57, 45, 21, 21, 89]

for i,j in enumerate(l3,100):
    if j == 21:
        print(i)

    print((i,j))

# for i,j in zip(range(5),range(5)):
#     print(i,j)
index = [i for i,j in enumerate(l3,100) if j == 21]

print(index)