for i in range(1,6):
    for j in range(5,i,-1):
        print("_",end="")
    for j in range(i,2*i-1):
        print(j,end="")
    for j in range(2*i-1,i-1,-1):
        print(j,end="")
    print()