# # for(i=1 ; i<=100 ; i++)
# # for( ; i!=100 ; )

# for vishv in range(10):   # start -> 0 (default), End - (n-1) 9
#     print(vishv,end=' ')   # 0 1 2 3 4 5 6 7 8 9 

# print()

# for h in range(25,101):  # start - 25, End - 100
#     print(h,end=' ')   # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

# for k in range(101,25):
#     print(k)   # Blank

# for g in range(-2,-8):
#     print(g,end=' ')   # Blank

# for g in range(-8,-2):
#     print(g,end=' ')   # -8 -7 -6 -5 -4 -3

# for n in range(10,11):
#     print(n)  # 10

# print()

# for sd in range(10,15,1):   # start - 10, End - 14, step(n-1) 0
#     print(sd,end=' ')   # 10 11 12 13 14

# # Step ---> 
# print()

# for sd in range(10,30,2):   # start - 10, End - 29, step - 1
#     print(sd,end=' ')   # 10 12 14 16 18 20 22 24 26 28


# for jk in range(-9,-2,3):
#     print(jk,end=' ')   # -9  -6  -3


# print()

# for ty in range(-10, - 2, -2):
#     print(ty)    # No o/p

# print()

# for jk in range(-4, -9, -3):
#     print(jk)  # -4 -7

# for www in range(3,-3,2):
#     print(www)   # No o/p

# for n in range(-3,4,-3):
#     print(n)   # no o/p


# list1 = [10,20,30,340]


# for k in list1:
#     print(k)

# for h in range(len(list1)):
#     print(list1[h])



# for d in range(3):         # 0 to 2   # d = 2
#     for w in range(3):     # 0 to 2   # w = 2
#         if d == w:    # 2 == 2
#             break
#         print(w)   # 0 0 1
#     print(d)      # 0 1 2

# # 0  0  1  0   1   2


# # ---------------------------------
# print()
# print()
# for i in range(3): 
#     for j in range(i):  
#         print("Hello")
#         # exit()
#         if i == j:  
#             continue
#         print(j) 
#     print(i)  
 
# else:
#     print("Else Block is Executed")


# list1 = [10,20,30,404,50,60]

# for i in list1:
#     print(i)

# for i in list1:   # 10
#     for k in list1:
#         print((i,k),end=' ')


# i = 1
# while i<=4:
#     j = 0
#     while j<=3:
#         if i == j:
#             # print("sdnv nsdv")
#             continue
#         j+=1
#     print(j)
#     i+=1

# i = 5         
# while i<=10:    # i = 7
#     j = 5       # j = 7
#     while j<=i:  # 7<=6
#         if i == j:  # 6 == 6
#             j+=1    # 
#             break
#         j+=1  
#         print(j,end= ' ')
#     i+=1
#     print(i,end=' ')

# 6 6 7

# print("----------")
# for i in range(5):
#     for j in range(7):
#         if j % 3 == 1:
#             break
#     else:
#         print("Inner for else block executed")
    
#     if i > j:
#         break
#     print("i =",i,"j = ",j)
    
# else:
#     print("Outer for else block executed")


# -------------------------------------
num = 1
kum = 1
while num <= 5:

    while kum <= 4:
        if num == kum:
            kum+=1
            continue
        print(kum)
        kum+=1
    print(num)
    num += 1


# p = 1
# while p <= 10:
#     p+=1
#     if p == 5:
#         continue
#     print(p)


# p = 1
# while p <= 10:
    
#     j=25
#     while j<=30:
#         print(j)
#         j+=1

#     p+=1


i = 43


while -2:
    i+=1
    if i == 47:
        break
    print(i)