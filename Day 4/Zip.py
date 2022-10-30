names = ['Ana','Hugo','Valeria']
ages = [65,29,42]
cities = ['Lima','Madrid','Mexico']
merge = list(zip(names,ages,cities))
print(merge)

for name,age,city in merge:
    print(f"{name} is {age} years and lives in {city}")

spanish = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
english = ['one','two','three','four','five']
numeros = list(zip(spanish,portugues,english))
print(numeros)