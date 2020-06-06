n=int(input("Enter any number : "))
for i in range(n,0,-1):
    k=i
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()