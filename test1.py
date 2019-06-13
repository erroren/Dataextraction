# list1 = [1,2,[3,4]]
# print(list1)
# list2 = list1
# print(list2)
# list1.append(5)
# print(list1,list2)
# list1[2].append(3.5)
# print(list1,list2)
#
# import copy
# list1 = [1,2,[3,4]]
# print(list1)
# list2 = copy.copy(list1)
# print(list2)
# list1.append(5)
# print(list1,list2)
# list1[2].append(3.5)
# print(list1,list2)

threshold = 155
table = []
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
print(table)