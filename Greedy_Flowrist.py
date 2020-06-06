# minimum_cost=(current_purchase+previous_purchase)*c[i]
# cost = current_purchase

def get_Minimum_Cost(n,k,c):
    cost=0      
    c=sorted(c,reverse=True)   #Sorted list in descending order
    for i in range(0,n):
        cost=cost+(i//k+1)*c[i]    #(i//k+1) = previous_purchase
    return cost
n=int(input())      # n = Number of flowers
k=int(input())      # k = Number of friends
c=[]                # c = Price of Each flower
c=[int(x) for x in input().split()]
print(get_Minimum_Cost(n,k,c))