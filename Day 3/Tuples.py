my_tuple = (1,2,(10,20),4)
print(type(my_tuple))
print(my_tuple[2][1])
my_tuple = list(my_tuple)#Convert tuple to list
print(type(my_tuple))
t = (1,2,3,1)
x,y,z,a = t
print(x,y,z)
print(len(t))
print(t.count(3))
print(t.index(2))