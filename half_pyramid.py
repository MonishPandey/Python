for i in range(4):
    for j in range(3,i,-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()