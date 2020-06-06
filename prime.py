# Program to check it is PRIME no. or NOT
num=int(input("Enter any number : "))
if num>1:
    for i in range(2,num//2+1):
        if num%i==0:
            print("It is NOT a Prime Number")
            break
    else:
        print("It is a Prime Number")