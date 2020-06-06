def merge_the_tools(string, k):
    # your code goes here
    n=len(string)//k
    c=0
    for i in range(n):
        print(string[c:c+n])
        c+=n
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)