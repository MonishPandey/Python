string = input()
substring = input()

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        # print(string[i:i+len(substring)])
        count += 1
print(count)