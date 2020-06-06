# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3],[4,5,6],[1,2,3]))

average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average([1,2,3],[4,5,6],[1,2,3]))
