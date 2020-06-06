def EvenDivisor(x,y):
    i = 1
    while i <= x:
        if x%i==0 and i%2==0:
            print(i)
        i += 1
x , y = map(int , input().split())
EvenDivisor(x,y)