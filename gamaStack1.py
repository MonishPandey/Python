x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1 +=i
if sum1==y:
    for j in range(1,y):
        if y%j==0:
            sum2 +=j
    if sum2==x:
        print("Amicable")
    else:
        print("Not Amicable")
else:
        print("Not Amicable")