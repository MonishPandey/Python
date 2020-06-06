c=0
d=5
b=16
for i in range(5):
    for j in range(5):
        if(i==0): 
            c+=1
            print(c,end="   ")
        elif(j==4 ):
            c+=1
            print(c,end="  ")
        elif(i==4):
            print(c+d,end="  ")
            d-=1
        elif(j==0):
            print(b,end="  ")
            b-=1
        else:
            print("    ",end="")

    print()