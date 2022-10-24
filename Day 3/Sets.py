# my_set = set({1,2,3,4,5,(1,2,3),1,2})
my_set = set({1,2,3,4,5})
print(type(my_set))
print(my_set)
#Another way to declare a set
# my_set2 = {1,2,3}
# print(type(my_set2))
# print(my_set2)
print(len(my_set))
print(2 in my_set)#Check if 2 is in the set
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
s1.add(2)
s1.remove(1)
s1.discard(6)
s1.pop()
s1.clear()
print(s1)
