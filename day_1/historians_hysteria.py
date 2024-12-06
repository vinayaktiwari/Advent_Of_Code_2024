
import numpy as np


def countSumofDiff(locList1:list,loclist2:list) -> int:
    sorted_list1 = sorted(locList1)
    sorted_list2 = sorted(loclist2)
    print(sorted_list1)
    print(sorted_list2)
    difs = []
    for i, j in zip(sorted_list1,sorted_list2):
        if len(sorted_list1) != len(sorted_list2):
            print("lists are of not same size")
            break
            
        else:
            difs.append(abs(i-j))
    return np.sum(difs)
    
with open("day_1/text.txt", "r") as file:
    list1 = []
    list2 = []
    
    for line in file:
        # Split the line into two values
        v = line.split()
        if len(v) == 2:
            list1.append(int(v[0]))
            list2.append(int(v[1]))

print("List 1:", len(list1))
print("List 2:", len(list2))


ans =countSumofDiff(list1,list2)


print("============DAY_1 ANSWER==========",ans)