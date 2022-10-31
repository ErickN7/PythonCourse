word = 'python'
listA = [letter for letter in word]
print(listA)

listB = [n for n in range(0,21,2)]
print(listB)

listC = [n/2 for n in range(0,21,2)]
print(listC)

listD = [n for n in range(0,21,2) if n * 2 > 10]
print(listD)

listE = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(listE)

feet = [10,20,30,40,50]
meters = [p * 3.281 for p in feet]
print(meters)
