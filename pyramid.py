len = input("Enter max length of pyramid:")
len = int (len)
for k in range (0, len+1):
    for i in range (0,k):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\n")
    for i in range (k, 0, -1):
        for j in range(0, i -1):
            print("*", end = ' ')
        print("\n")