n=int(input("Enter any number : "))
for i in range(n):
    for j in range(n):
        if (i==j or i+j==4):
            print("1",end="")
        else:
            print("0",end="")
    print()