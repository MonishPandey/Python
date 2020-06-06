def arrangeStudents(b, g):
    flag = 0
    i = 1
    test_list=b+g
    test_list.sort()
    while i < len(test_list): 
        if(test_list[i] < test_list[i - 1]): 
            flag = 1
        i += 1
    if flag == 0 : 
        return "Yes"
    else : 
        return "No"
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        b = list(map(int, input().rstrip().split()))
        g = list(map(int, input().rstrip().split()))
        result = arrangeStudents(b, g)
        print(result)
