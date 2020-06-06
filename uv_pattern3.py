for i in range(1,5):
    for j in range(1,10):
        if(i==j or i+j==10):
            print(i,end="")
        else:
            print(" ",end="")
    print()
x=y=5
for i in range(1,6):
    for j in range(1,10):
        if (j==y or j==x):
            print(x,end="")
        else:
            print(" ",end="")
    x-=1
    y+=1
    print()