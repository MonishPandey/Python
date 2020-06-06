for i in range(9):
    if i<5:
        for k in range(1,i+2):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
    else:
        for k in range(9,i,-1):
            print(" ",end="")
        for j in range(9,i,-1):
            print("*",end="")

    print()