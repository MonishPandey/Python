st=input("Enter any string : ")
out=''
for n in st:
    if n not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out+=n
    else:
        k=ord(n)
        l=k+32
        out+=chr(l)
print("String into Lower case: ",out,end="")