l1 = [[10,90,89],
      [20,30,89],
      [30,78,21],
      [67,45,34]]

for row in range(len(l1)):   # 0 to 3
    if row % 2 == 0:
        for col in range(len(l1[row])):  # 0 to 2
            print(l1[row][col],end=' ')
    else:
        for col in range(len(l1[row])-1, -1, -1):  # 0 to 2
            print(l1[row][col],end=' ')
    print()
