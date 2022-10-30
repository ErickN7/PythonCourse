# coins = 5
#
# while coins > 0:
#     print(f"Tengo {coins} coins")
#     coins -= 1
# else:
#     print("I don't have more coins")

response = 'x'
while response == 'y':
    # response = input("Do you want to continue? (y/n)")
    pass#Is like a
    # break #Break the while loop
else:
    print("Thank you")

name = 'Hello'
for letter in name:
    if letter == 'e':
        # break#Break the while/for loop
        continue
    print(letter)