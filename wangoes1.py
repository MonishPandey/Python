for i in range(1,6):
    odd=1
    even=0
    for j in range(1,i+1):
        if i%2==1:
            print(odd,end=" ")
            odd+=2
        else:
            even+=2
            print(even,end=" ")
    print()