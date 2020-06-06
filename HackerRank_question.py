''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
# Custom Case Input:2 
# 2 10 3 6 7 5 3 5 6 2 9 1 2 7 0 9 3 
# 6  0 6 2 6 5 2 4 8 5 4 9 0 2 1 1 7
# Custom Case Output:7
# 4
# 3 6 7 5 3 5 6 2 9 1 
# 2 7 0 9 3 6 0 6 2 6 

# 2 21 23 431 
# 2 33 2  1
def main():
# Write code here 
    c=0
    T=int(input())
    N=int(input())
    for i in range(T):
        l3=[]
        l4=[]
        l1=[int(x) for x in input().split()]
        l2=[int(x) for x in input().split()]
        l1.sort()
        l2.sort()
        for i in range(N):
            if l1[i]>l2[i]:
                c+=1
            else:
                l3.append(l1[i])
                l4.append(l2[i])
        l3.reverse()
        for i in range(N-c):
            if l3[i]>l4[i]:
                c+=1
    print(c)
main()

