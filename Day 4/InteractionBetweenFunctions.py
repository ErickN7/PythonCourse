from random import shuffle
#Initial List
sticks = ['-','--','---','----']

#Mix sticks

def mix(listA):
    shuffle(listA)
    return listA

#Try your luck

def try_your_luck():
    attempt = ''
    while attempt not in ['1','2','3','4']:
        attempt = input('Choose a number between 1 and 4: ')

    return int(attempt)

#Check attempt

def check_attempt(listA,attempt):
    if listA[attempt - 1] == '-':
        print('You have to wash the dishes')
    else:
        print("You don't have to wash the dishes")
    print(f'Your choice was {listA[attempt - 1]}')

# mixed_sticks = mix(sticks)
# choice = try_your_luck()
# check_attempt(mixed_sticks, choice)

#Exercise 100
from random import randint

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return (dado1, dado2)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados in range(7, 10):
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


dado1, dado2 = lanzar_dados()
result = evaluar_jugada(dado1, dado2)

#Exercise 101
def reducir_lista(lista_numeros):
    l = list(set(lista_numeros))
    mx = max(l)
    l.remove(mx)
    return l

def promedio(listA):
    result = 0
    listA = list(listA)
    for n in listA:
        result += n
    return  result / len(listA)

lista_numeros = [32,43,3,4,5,3,2]
p = reducir_lista(lista_numeros)
res = promedio(p)
print(res)

#Exercise 102
from random import choice
def lanzar_moneda():
    choices = ['Cara','Cruz']
    your_choice = choice(choices)
    return your_choice

def probar_suerte(your_choice: str, listA: list):
    if your_choice.lower() == 'cara':
        print('La lista se autodestruirá')
        listA.clear()
    else:
        print("La lista fue salvada")
    return listA

lista_numeros = [2,4,5,6]
aux = lanzar_moneda()
res102 = probar_suerte(aux, lista_numeros)