from random import randint
name = input('Hello, What is your name? ')
number = randint(1,100)
print(f"Hi {name}. Guess the number that I'm thinking xD. You have 8 attempts")
attempt = 1

while attempt <= 9:
    if attempt > 8:
       print(f'You lose. The number I was thinking of was {number}')
       break

    print(f"This is your {attempt} attempt")
    guess_number = int(input("Tell me the number that I'm thinking: "))

    if guess_number not in range(1,101):
        print('Your number is out of range, it must be between 1 and 100')
    elif guess_number == number:
        print('You win')
        break
    elif guess_number < number:
        print("The number that I'm thinking is greater than the one you provided")
    elif guess_number > number:
        print("The number that I'm thinking is less than the one you provided")

    attempt += 1
