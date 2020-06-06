def Ifpossible(x,y) : 
   c=1
   s=0
   if s+x == y:
      s+=c
      c=c*3
      return 1
   else:
      return 0
x=int(input())      
y=int(input())
print(Ifpossible(x,y))