n=int(input("Enter any number : "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(6,i,-1):
        print(i,end="")
        i+=1
    print()