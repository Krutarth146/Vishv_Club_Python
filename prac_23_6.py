# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Expected Result : 2

sample =  ['abc', 'xyz', 'aba', '1221']
count = 0

for i in sample:
    if len(i) >= 2 and i[0] == i[-1]:
        count+=1

print(count)  # 2
 
sam = [i for i in sample if len(i) >= 2 and i[0] == i[-1]]
print(sam)


List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i][1] > List[j][1]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

print(List)  # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


list1 = ["Dhaval", 'Sahil', 'Yash', 'Manoj', 'Ashok', 'Raman']
res = []


for i in range(len(list1)):
    if i == 0 or i == 4 or i == 5:
        continue
    res.append(list1[i])

print(res)   # ['Sahil', 'Yash', 'Manoj']


# # Take input from User using List Comprehension

# l1 = [int(float(i)) for i in input().split('_')]
# # l2 = list(i for i in input())

# print(l1)



l1 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

d2 = []

for i in range(3):
    temp = [int(j) for j in input().split()]
    # print(temp)
    d2.append(temp)
    print(d2)
    temp = []
print(d2)   # [[10, 9089, 88], [21, 32, 45], [21, 89, 78]]


# Power , Factorial 5! = 120 , FIbonnacci ---> 0 1 1 2 3 5 8 ....


