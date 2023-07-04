k = [i for i in range(1,6)]
print(k)   # [1, 2, 3, 4, 5]


list1 = [10,20,30,40,50]

l = [k1 for k1 in list1]
print(l)  # [10, 20, 30, 40, 50]

l = [k1 for k1 in list1 if k1 % 30 == 0]
print(l)   # 30

counter = 0

for j in range(4):
    for l in range(3):
        for q in range(3):
            pass
            # print(q)
            counter += 1

print(counter)  # 36


hj = [(j,l,q) for j in range(4) for l in range(3) for q in range(3)]
print(hj)



l1 = [10,20,30,40]

f1 = [j for i,j in enumerate(l1,0) if i % 2 != 0]
print(f1)   # [20, 40]


l2 = [10,20,30,40,50,60,90]
l3 = [108,280,307,405,504,601]

l1 = [(k,l) for k,l in zip(l2,l3)]
print(l1) # [(10, 108), (20, 280), (30, 307), (40, 405), (50, 504), (60, 601)]