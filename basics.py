#example for .extend() method
original_list=[1,2,3]
appendlist=[4,5,6]
newlist=[]

# newlist.append(appendlist)
# print(newlist)

original_list.extend(appendlist)
print(original_list)

newlist.extend(appendlist)
print(newlist)


original_list.append(appendlist)
print(original_list)

