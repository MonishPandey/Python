def is_palindgrome(name):
    reverse=name[::-1]
    if reverse == name:
        print("palindgrome")
    else:
        print("Not_Palindgrome")

Original_String=input("Enter any Name : ")
is_palindgrome(Original_String)