for r in range(5,0,-1):
    for c in range(r,0,-1):
        print(c,end="")
        if c>1:
            print("*",end="")
    print()     