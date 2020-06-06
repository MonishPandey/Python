string="geekfor"
for i in range(7):
    for j in range(i):
        if (i<=3):
            print("*",end="")
    if (i>3):
        for k in range(6,i,-1):
            print("*",end="")
    print(string[i])