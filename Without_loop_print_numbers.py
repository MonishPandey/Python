def loop(n):
    if (n>0):
        loop(n-1)
        print(n,end=" ")
n=int(input("Enter a limit: "))
loop(n)