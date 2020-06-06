def hourglassSum(arr):
    sum = 0
    for i in range(4):
        for j in range(4):
            top=arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle = arr[i + 1][j + 1]
            bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]   
            if ((top + middle + bottom) > sum):
                sum = top + middle + bottom
    return sum
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(str(result) + '\n')