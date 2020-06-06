def isSphenic(number):
    result=False
    listFactor=[]
    i = 2
    while number > 1:
        count = 0
        while number % i == 0:
            count +=1
            number = int(number/i)
        if count ==1:
            listFactor.append(i)
        if len(listFactor) == 3:
            break
        i +=1
    if len(listFactor) == 3:
        print(listFactor)
        result=True
    return result
number=int(input("Enter any number : "))
print(f"{number} is Sphenic ? {isSphenic(number)}")