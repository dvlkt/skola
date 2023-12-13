import random

# 1. Funkcija, kas atrod saraksta maksimālo vērtību
def max(a):
    highest = None
    for i in a:
        if highest == None or i > highest:
            highest = i
    return highest
print(max([3, 7, 4, 2, 3, 4]))

# 2. Funkcija, kas atrod saraksta minimālo vērtību
def min(a):
    lowest = None
    for i in a:
        if lowest == None or i < lowest:
            lowest = i
    return lowest
print(min([9, 4, 8, 1, 5, 3]))
print(min([]))

# 3. Funkcija, kas apmaina divu globālu mainīgo vērtības vietām
a = int(random.random()*100)
b = int(random.random()*100)
def swap():
    global a, b
    temp = a
    a = b
    b = temp
print(a, b)
swap()
print(a, b)

