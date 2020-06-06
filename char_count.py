def char_finder(String):
    count={}
    for char in String:
        count[char]=String.count(char)
    return count
print(char_finder("harshit"))