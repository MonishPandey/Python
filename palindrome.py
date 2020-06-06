# Program to check a Plindrom
n=input("Enter any String or Number : ")
name=n.lower()
for i in range(len(name)):
    reverse=name[::-1]
if name==reverse:
    print("Plindrome")
else:
    print("Not a Plindrome")