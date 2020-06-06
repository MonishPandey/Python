n=int(input("Input : "))
for i in range(1,n//2+2):
    for j in range(1,i+1):
        if j!=1:
            print(f"*{j}",end="")
        else:
            print(j,end="")
    print()
for i in range(1,5):
    count=0
    for j in range(5,i,-1):
        count+=1
        if j!=5:
            print(f"*{count}",end="")
        else:
            print(count,end="")
    print()