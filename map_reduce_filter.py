def cube(ele):
    return ele ** 3

list1 = [10,90,43,67,22]

vishv = list(map(cube,list1))
print(vishv)   # [1000, 729000, 79507, 300763, 10648]


vishv = list(map(lambda x : x + 1200, list1))
print(vishv)   # [1210, 1290, 1243, 1267, 1222]


# ---------------------------------------

list1 = [10,90,43,67,22]

raval = list(map(lambda ele : ele % 2 != 0,list1))
print(raval)   # [False, False, True, True, False]


raval = list(filter(lambda ele : ele % 2 != 0,list1))
print(raval)   # [43, 67]


# --------------------------------
list1 = [10,90,43,67,22]


from functools import reduce

patel = reduce(lambda n1, n2 : n1 + n2, list1)
print(patel)   # 232

from itertools import accumulate

royal = list(accumulate(list1, lambda n1, n2 : n1 + n2))
print(royal)  # [10, 100, 143, 210, 232]




# -----------------------------------------


def fun1(f4):   # We can pass function as an Argument
    print("This is fun1 Function")
    f4()

def aman():
    print("This is Aman Function")

raval = aman
fun1(raval)


# Inner Function

def Vishv(f9):   # We can Make function inside a FUnction

    def Manoj():
        print("This is Manoj Function")
        f9()

    return Manoj()


@Vishv    # Decorator
def kru():
    print("This is Kru Function")

# Vishv(kru)



# @classmethod
# def raval():
#     print("Hello")



# Recursion

# when function calls itself then it is called Recursion