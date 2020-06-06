largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest < num or largest==None:
        	largest=num 
        elif smallest > num or smallest == None:
        	smallest=num
    except:
        print("Invalid input")

print("Maximum is",largest)
print("Minimum is",smallest)