# 1
# 2*3
# 4*5*6
# 7*8*9*10
# 7*8*9*10
# 4*5*6
# 2*3
# 1
count=0
for i in range(4):
    for j in range(i+1):
        count+=1
        if j!=0:
            print(f"*{count}",end="")
        else:
            print(count,end="")
    print()
count=0     
for i in range(1,5):
    count+=i            #1+2+3+4=10
for i in range(4):
    count=count-4+i     #10-4+0=6
    count1=count
    for j in range(4,i,-1):
        count+=1
        if j!=4:
            print(f"*{count}",end="")
        else:
            print(count,end="")
    print()
    count=count1