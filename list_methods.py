# # List ---> Allow's Duplicates, Ordered (Indexed), Mutable (Chnageble)

# list1 = []
# print(type(list1))  # <class 'list'>

# l2 = [10,10,20,30,True,78+8j]
# l3 = [10,10,20,30,True,78+8j]

# print(len(l2))  # 6 ---> Length starts from 1 & Index starts from 0
# print(l2.__sizeof__())  # 88
# print(id(l2))  # 2317685892736
# print(id(l3))  # 1686201224000

# l3 = l2   # Deep Copy

# x = 90
# f = 90

# print(id(x))  # 2911004658704
# print(id(f))  # 2911004658704

# if x is f:   # Identity O/p
#     print("x is f")

# if l2 is l3:
#     print("l2 is l3")  # l2 is l3


# vishv = l2    # Deep Copy  (phy Adhar Card == Digilocker)
# manoj = l2.copy()   # Shallow COpy (phy Adhar card == xerox)

# l2.append("Royal")

# print(l2)     # [10, 10, 20, 30, True, (78+8j), 'Royal']
# print(vishv)  # [10, 10, 20, 30, True, (78+8j), 'Royal']
# print(manoj)  # [10, 10, 20, 30, True, (78+8j)]

# vishv.append(5000)
# print(l2)

# l1 = [10,20,30,40]

# l1+=[900,89,78,'str']

# print(l1)  # [10, 20, 30, 40, 900, 89, 78, 'str']

# l1.append("True")
# print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True']

# l1.extend("str1")
# print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1']


# temp = [89, 67, 8945]

# l1.append(temp)
# print(l1)    # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945]]

# # l1.extend(temp)
# # print(l1)    # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', 89, 67, 8945]

# # l1.extend(4500) # int object is not Iterable Gives Error
# l1.extend([4500])
# print(l1)   # [10, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 4500]


# l1.insert(1, 7800)
# print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 4500]

# l1.insert(-1, 9000)
# print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 9000, 4500]

# l1[-1] = 789363 
# print(l1)   # [10, 7800, 20, 30, 40, 900, 89, 78, 'str', 'True', 's', 't', 'r', '1', [89, 67, 8945], 9000, 789363]

# # del l1   delete whole l1



# # Remove Elements

# del l1[8:]
# print(l1)  # [10, 7800, 20, 30, 40, 900, 89, 78]

# print(l1.pop())  # 78
# print(l1)   # [10, 7800, 20, 30, 40, 900, 89]

# l1.pop(3)
# print(l1)   # [10, 7800, 20, 40, 900, 89]

# l1.remove(7800)
# print(l1)   # [10, 20, 40, 900, 89]

# # -------------------


# # l1.sort()   # default ---> Increasing order
# # print(l1)   # [10, 20, 40, 89, 900]

# # l1.reverse()
# # print(l1)   # [900, 89, 40, 20, 10]

# l1.sort(reverse=True)
# print(l1)   # [900, 89, 40, 20, 10]

# # l1.clear() # Clear l1

# print(l1.count(900))  # 1   # frequency
# print(l1.index(900))  # 0   # Index (Position)


# for i in l1:
#     print(i)

# for d in range(len(l1)):  # start - 0, end = 4
#     print(l1[d],end=' ')   # 900 89 40 20 10


# def pangrams(s):

#     list1 = [chr(i) for i in range(97,123)]
#     list1.append(' ')
    
#     s = s.lower()
#     for i in list1:

#         if i.lower() not in s:
#             return "not pangram"
#     else:
#         return "pangram"
    

# print(pangrams('The quick brown fox jumps over the lazy Dog'))




# A non-negative integer is said to be a cyclops number if it 
#     consists of an odd number of digits, the middle digit 
#     (more poetically, the “eye”) is a zero, and all other 
#     digits of that number are non-zero.

#     Return True if the input is a cyclops number, and False
#     otherwise.

#     Note 1: Functions that return True/False are unlikely to 
#     appear on a test, since you can achieve at least 50% by
#     simply saying 'return True' or 'return False'...

#     Note 2: This problem comes from Ilkka Kokkarinen's 
#     excellent set of "109 Python Problems for CCPS 109". The 
#     full set can be found at his github, and are great practice.

#     https://github.com/ikokkari/PythonProblems

#     Many (or most) of his problems are quite difficult, so be
#     ready for a challenge if you attempt them.
# n_str=str(n)
#     eye=len(n_str)//2
#     if len(n_str)%2!=0 and n_str[eye]=='0':
#             left_part=[i for i in n_str[0:eye] if i!='0']
#             right_part=[j for j in n_str[eye+1:]if j!='0']
#             if len(left_part)==len(n_str)//2 and len(right_part)==len(n_str)//2:
#                 return True
           
#             return False 
#     return False



def check_cyclops(num):
    flag = 0
    num = str(num)
    if len(str(num)) & 1 != 0:
        if num[(len(num) // 2)] == '0':
            if num.count('0') > 1:
                flag = 1
        else:
            flag = 1
    else:
        flag = 1

    if flag == 0:
        return 100, 'Granted'
    else:
        return 0, 'Not Granted'


def Vishv():
    a = 'w'
    k = 3
    print(a*k)  # www

if check_cyclops(45021):
    Vishv()


print(check_cyclops(12)[1][:3])


l3 = [(10,20), (20,30), (33,90)]

flag = 0
for k in range(len(l3)-1):
    if l3[k][-1] != l3[k+1][0]:
        flag = 1
        break
    else:
        flag = 0

if flag == 0:
    print(True)




tup1 = ((5,6), (5,7), (5,90), (6,10,6), (6,5), (9,6), (70,10))
# ans = ((5,6,7,90), (6,5,10), (9,6), (70,10))

