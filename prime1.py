c=0
n=int(input("Enter any number : "))
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")