# def Vishv(num):
#     for i in range(1,num+1):
#         print(i)


# Vishv(5)  # 1 2 3 4 5   


# def Vishv1(num):
#     list1 = []
#     for i in range(1,num+1):  # 1,6  ---> 1 to 5
#         list1.append(i)
#     return list1   # 1
    

# print(Vishv1(5))   # [1, 2, 3, 4, 5]


def raval(num):
    for i in range(1,num+1):
        yield i

# print(raval(5))   # <generator object raval at 0x00000200BE509A10>
# print(raval(5).__next__())   # 1
# print(raval(5).__next__())   # 1


# x = raval(5)
# print(x.__next__())  # 1   # Generator
# print(x.__next__())  # 2
# print(x.__next__())  # 3

for i in raval(5):
    print(i)


# Lambda  (Anounoumous Function)

num = 90

# def sq(num):
#     return num**2

# print(sq(num))   # 8100


square = lambda num : num * num

print(square(num))
print(type(square))   # <class 'function'>

royal = lambda x,y = 2 : x**y

print(royal(32))   # 1024


# Quadratic Function   (a*x**2) + (b*x) + c

def quadratic_fun(a1,b1,c1):
    return lambda x : (a1*x**2) + (b1*x) + c1


patel = quadratic_fun(10,20,30)

print(patel(3))  # 180

# Nested Lambda

Manoj = lambda x,y= 4: lambda a,b,c : a*x**2 + b*x + c + y

ramesh = Manoj(5,4)

print(ramesh(10,22,11))  # 250 + 110 + 11 + 4 ---> 375

print(Manoj(5)(10,22,11))  # 375


# ---------------------------------------


num = 90

def sq(num):
    return num**2

list1 = [10,33,22,55,11,77,8,89,99,99]

def sq1(lst):   # For whole List
    square_l = []
    for ele in lst:
        square_l.append(ele**2)
    return square_l

def sq2(ele):   # For Individual ELement
    return ele ** 2

# Powerful Functions  Map, Reduce, Filter

r1 = list(map(sq2, list1))
# print(r1)   # <map object at 0x000001E4F0157C40>
# print(type(r1))   # <class 'map'>


r2 = list(map(lambda x : x ** 2, list1))
print(r1)  # [100, 1089, 484, 3025, 121, 5929, 64, 7921, 9801, 9801]
print(r2)  # [100, 1089, 484, 3025, 121, 5929, 64, 7921, 9801, 9801]