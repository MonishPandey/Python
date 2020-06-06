for i in range(5):
    for j in range(4,i,-1):
        print(" ",end="")
    for k in range(2*i+1):
        print(abs(i),end="")
        i=i-1
    print()