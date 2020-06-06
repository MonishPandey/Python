for i in range(1,11):
    for j in range(i):
        if i<6:
            print("*",end="")
        # if i==5:
            # print("*",end="")
    if i>5:
        for k in range(1,11):
            if k<5:
                print(" ",end="")
            if i<=k:
                print("*",end="")
    print()
