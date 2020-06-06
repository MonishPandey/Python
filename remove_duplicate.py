def Remove_Duplicate(list1):
    final_list=[]
    for i in list1:
        if i not in final_list:
            final_list.append(i)
    return final_list
list1=[int (x) for x in input("Enter space seperated Elements: ").split(" ")]
print(Remove_Duplicate(list1))