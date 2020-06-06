def func(*args):
    if args==True:
        print()
    else:   
        return [i.capitalize() for i in args]
names=["mohit","rohit"]
print(func(*names))