
num=153
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num == sum:
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")