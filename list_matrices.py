list1 = [[103,204,30], 
         [41,502,60], 
         [708,80,905]]


print(list1[1][2])    # 60
# print(list1[1][3])    # Error

d1list = []

for i in list1:
    for k in i:
        print(k,end=' ')   # 10 20 30 40 50 60 70 80 90
        d1list.append(k)


print(d1list)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]



list1 = [
         [103,204,30], 
         [41,502,60], 
         [708,80,905]
        ]

# list1.sort()

print(list1)   # [[41, 502, 60], [103, 204, 30], [708, 80, 905]]

d1 = []

for exer in list1:
    for inte in exer:
        d1.append(inte)


print(d1)   # [103, 204, 30, 41, 502, 60, 708, 80, 905]

d1.sort()

print(d1)   # [30, 41, 60, 80, 103, 204, 502, 708, 905]


list2 = list1
k = 0

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list2[i][j] = d1[k]   # list2[1][0] = d1[3]
        k+=1

print(list2)   # [[30, 41, 60], [80, 103, 204], [502, 708, 905]]


sorted_list = [[], [], []]
k = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        sorted_list[i].append(d1[k])   
        k+=1

print(list2)   # [[30, 41, 60], [80, 103, 204], [502, 708, 905]]