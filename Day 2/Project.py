name = input("Give me your name: ")
sale = float(input("Give me the total amount of your sales of this month: "))
commission = round((sale * 13) / 100, 2)
print(f"Hi {name} your commission for your sales of this month is: {commission}")