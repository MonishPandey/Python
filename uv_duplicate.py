def repeated_list(l):
    repeated=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j] and l[i] not in repeated:
                repeated.append(l[i])
    return repeated
list=[int (x) for x in input("Enter elements of list : ").split()]
# list1=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
print(repeated_list(list))