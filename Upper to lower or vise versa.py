def swap_case(s):
    result=""
    for i in s:
        if i.isupper():
            l=ord(i)+32
            result+=chr(l)
        elif i.islower():
            l=ord(i)-32
            result+=chr(l)
        else:
            result+=i
    return result

s = input()
result = swap_case(s)
print(result)