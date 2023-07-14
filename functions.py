
# 1. Func. Defination
# 2. Func. Calling

# print(), input(), len(), id(), min() ----> Inbuilt


# Func. Types
# 1. Without return Type and Without Arguments
# 2. With return Type and Without Arguments
# 3. Without return Type and With Arguments
# 4. With return Type and With Arguments


# void Vishv()
# {
#     // statements
# }


# 1. Without return Type and Without Arguments
def Vishv():
    num1,num2,num3 = 90,78,"Manoj"
    print(num1+num2,num3)

Vishv()   # 168 Manoj


x = 90   # Global variable

def jk(): 
    global x
    # x = 30   # local variable
    x += 20
    print(x)   # 110

print(jk())   # None
x+=40
print(x)  # 150

# 2. With return Type and Without Arguments

def royal():
    return 50

print(royal())

x = royal()
print(x)


def raval():
    return "Vishv",[10,20,30],{"Name" : True}

print(raval())  # ('Vishv', [10, 20, 30], {'Name': True})
x = raval()  # ('Vishv', [10, 20, 30], {'Name': True})
print(x[-1]['Name'])  # True


# 4. With return Type and With Arguments
def Jalp(num):
    return num ** 2

print(Jalp(5))   # 25

def Jalp(num):
    for k in range(1, num+1):
        yield k   # Generator


# print(Jalp(5))


# print(Jalp(5))   # <generator object Jalp at 0x000001F2D5009A10>

# print(Jalp(5).__next__())
# print(Jalp(5).__next__())

# for i in Jalp(5):
#     print(i)

# 3. Without return Type and With Arguments

def patel(num1, num2, num3 = 50):  # Default Function
    print(num1 + num2 + num3)

patel(90,78,10)  # 178


# def patel(n1 = 90, n2, n3 = 50):
    # pass

# patel( ,50, )


def raval(num1, *vishv, num4 = 89):
    """Args"""
    print(vishv)   # (10, 20, 30.78, True, [10, 2030, 40])
    print(type(vishv))  # <class 'tuple'>

    for k in vishv:
        print(k)

    print(type(vishv[-1]))  # list


raval(10,20,30.78,True,[10,2030,40])
print(raval.__doc__)  # Args 

def manoj(*args ,**kru):
    """kwargs"""
    print(kru)   #  {'name': 'Manoj', 'roll': [10, 20, 30], 'address': 'Ahm'}
    # type - Dict

    print(kru['roll'][-2])   # 20

    for k in kru:
        print(k)

    for k in kru.values():
        print(k)

    for k in kru.items():
        print(k)

manoj(10,20,30,40,50, name = "Manoj", roll = [10,20,30], address = "Ahm")

