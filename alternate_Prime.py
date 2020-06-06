def prime(num):
    f=0
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            f = 1
            break
    if f == 0:
        return 1
    else:
        return 0
def print_alternate_prime(n):
    count=0
    for num in range(2,n+1):
        if prime(num) == 1:
            if count % 2 == 0:
                print(num,end=" ")
            count+=1
n=int(input("Enter any numbers : "))
print_alternate_prime(n)