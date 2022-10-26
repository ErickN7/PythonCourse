if 10 > 9:
    print('Is correct')
else:
    print('Is incorrect')

pet = 'dog'

if pet == 'cat':
    print("You have a cat")
elif pet == 'dog':
    print("You have a dog")
else:
    print("I don't know what animal you have")

age = 16
score = 9

if age < 18:
    print("You are underage")
    if score >= 7:
        print("Approved")
    else:
        print("Not approved")
else:
    print("You are an adult")