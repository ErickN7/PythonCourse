from random import *

randomA = randint(1,50)
print(randomA)

randomB = round(uniform(1,5), 1)
print(randomB)

randomC = random()
print(randomC)

colors = ['azul', 'rojo', 'verde', 'amarillo']
randomD = choice(colors)
print(randomD)

numbers = list(range(5,50,5))
shuffle(numbers)
print(numbers)