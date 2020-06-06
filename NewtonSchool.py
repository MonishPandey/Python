def equationSum(N):
   c=0
   for X in range(1,N+1):
      c+=((X+1)**2 - (3*X + 1) + X)
   return c