def main():
    T=int(input())
    N=int(input())
    if 1<= T and T <=100000 and 1<= N and N <=100000:
        count=0
        for i in range(T):
            l1=list(map(int,input().split()))
            l2=list(map(int,input().split()))
            l1.sort()
            l2.sort()
            for i in range(N):
                for k in range(len(l2)):
                    if l1[i]>l2[k]:
                        count+=1
                        l2.pop(k)
                        break
    print(count)
main()