my_list = ['a', 'b', 'c']
other_list = ['Hola', 5, 354.2]
print(type(my_list))
result = len(my_list)
print(result)
print(my_list[2])
print(other_list[0:2])
my_list3 = my_list + other_list
print(my_list3)

my_list3[0] = 'z'
my_list3.append('q')
erased = my_list3.pop(0);
print(my_list3)
print(erased)

list2 = ['g', 'o', 'b', 'm', 'c']
list2.sort()
print(list2)
list2.reverse()
print(list2)