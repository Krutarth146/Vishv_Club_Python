# Fibonacci

# 0 1 1 2 3 5 8 13 .......

# n1,n2 = 0,1

# print(n1,n2,end=' ')

# i = 10
# while i<=18:
#     n3 = n1 + n2
#     print(n3,end=' ')
#     n1 = n2
#     n2 = n3
#     i+=1

# -----------------------------
print()

list1 = [0,1]

for i in range(9):
    list1.append(list1[-1] + list1[-2])

print(list1[-2]) 
print(list1)



# ------------------

num=1
while  num<=1000:  
    k=2
    flag=0
    while k<num:
        if num%k==0:
            flag=1
            break
        k+=1
    if flag==0 and num != 1:
       print(num,end=' ')
    num+=1



# ------------------------------------------

l1 = [10,20,30,40,50,60]

for i in l1:
    print(i)

for j in range(len(l1)):
    print(l1[j])