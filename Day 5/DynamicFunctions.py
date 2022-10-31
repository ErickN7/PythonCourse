def check_3_values(number):
    return number in range(100,1000)

def check_3_values_list(listA):
    for n in listA:
        if n in range(100,1000):
            return True
    return False

def check_3_values_list_A(listA):
    listB = []
    for n in listA:
        if n in range(100,1000):
            listB.append(n)
    return listB

result = check_3_values(494)
print(result)
resultA = check_3_values_list([23,54,3434])
print(resultA)
resultB = check_3_values_list_A([23,544,3434])
print(resultB)

prices_coffee = [('capuchino',1.5),('Expresso',1.2),('Moka',1.9)]

def coffe_most_expensive(list_prices):
    price_higher = 0
    coffee_more_expensive = ''

    for coffe,price in list_prices:
        if price > price_higher:
            price_higher = price
            coffee_more_expensive = coffe
    return (coffee_more_expensive, price_higher)

coffee, price = coffe_most_expensive(prices_coffee)
print(f'The coffee more expensive is {coffee} which price is {price}')