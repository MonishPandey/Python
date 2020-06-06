for r in range(5):
    for k in range(5,r+1,-1):
        print("_",end="")
    for c in range(r+1):
        if ((c==4) or (c==0 and r<1) or (c==2 and r>1)):
            print("0",end="")
        else:
            print("1",end="")
    print()