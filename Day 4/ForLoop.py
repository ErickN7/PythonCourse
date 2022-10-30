list = ['a','b','c']

for letter in list:
    number_letter = list.index(letter) + 1
    print(f"Letra {number_letter}: {letter}")

list2 = ['Pablo','Laura','Luis','Fede','Julia']

for name in list2:
    if name.startswith('L'):
        print(name)
    else:
        print('Nombre que no comienza con L')

list3 = [1,2,3,4,5]
my_value = 0

for number in list3:
    my_value += number
print(my_value)

word = 'python'
for letter in word:
    print(letter)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = { 'clave1': 'a', 'clave2': 'b','clave3': 'c'}

for item in dic.items():
    print(item)

