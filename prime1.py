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
