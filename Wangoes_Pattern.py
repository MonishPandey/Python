for r in range(5):
    for c in range(r+1):
        if (c==0 or c==4 or (c==2 and r>1)):
            print("0",end="")
        else:
            print("1",end="")
    for k in range(8,2*r+1,-1):
        print("_",end="")
    for c in range(r+1):
        if (c==0 or c==4 or (c==2 and r>1)):
            print("0",end="")
        else:
            print("1",end="")
    print()