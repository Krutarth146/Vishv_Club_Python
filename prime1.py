# Prime Numbers : 

# 2 - 1,2
# 24 - 1, 2, 3, 4, 6, 8, 12, 24
# 23 - 1, 23
# 29 - 1, 29
# 32 - 1, 2, 4, 8, 16, 32


num = 32
counter = 0

for i in range(1,num+1):
    if num % i == 0:
        print(i)
        counter += 1
print()
print(counter)  # 12

if counter == 2:
    print("Prime")


# Prime Number


num = 23   # 1, 23

for i in range(2,num):
    if num % i == 0:
        break

if i == (num-1):
    print("Prime Number")
else:
    print("Not Prime Number")


# ------------
num = 23   # 1, 23
flag = 0

for i in range(2,num):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print("Not Prime Number")
else:
    print("Prime Number")


# 1 to 10000 Prime Numbers  # ----->   2 3 5 7 11 13 17 19 23 29 31 37 ........




num = 894

# while num != 0 :
while num > 0 :
    rem = num % 10  # rem = 8
    print(rem,end='')      # 498  # Reverse Print
    num = num // 10 # num = 0


# Sum of Digits
num = 894
sum = 0

while num > 0 :
    rem = num % 10    # rem = 8
    sum = sum + rem   # sum = 21
    num = num // 10   # num = 0
print(sum)


num = 894
count = 0

while num > 0 :
    count += 1
    num = num // 10   # num = 0
print(count)  # 3


num = 101
sum = 0

safe = num  

while num > 0 :
    rem = num % 10         # rem = 8 
    sum = sum * 10 + rem   # sum = 498
    num = num // 10        # num = 0

print(sum)  # 498

if sum == safe:
    print("Palindrome")


# Armstrong Number

# 153 ---> (1*1*1) + (5*5*5) + (3*3*3)
num = 8208
safe = num
safe1 = num


counter= 0
while safe > 0:
    counter+=1
    safe = safe // 10

length = len(str(num))


rev = 0

safe = num  

while num > 0 :
    rem = num % 10         # rem = 8 
    rev = rev + rem ** length   # sum = 498
    num = num // 10        # num = 0

print(rev)  # 498

if rev == safe1:
    print("Armstrong")

# Prime, Palindrome, Armstrong Number (1 to 10000)

# Perfect Number  6 ---> 1 + 2 + 3, 28 --> 1 + 2 + 4 + 7 + 14

# Twin Number  22 ---> 2 * 2 == 2 + 2

# num = 5, step = 6

# 5 + 55 + 555 + 5555 + 55555 + 555555 = (?)