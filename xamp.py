def get_Minimum_Cost(n,k,c):
    cost=0
    c=sorted(c,reverse=True)
    print(c)
    for i in range(0,n):
        cost=cost+(i//k+1)*c[i]
        print(cost)
    return cost
n=int(input())
k=int(input())
c=[]
c=[int(x) for x in input().split()]
print(get_Minimum_Cost(n,k,c))