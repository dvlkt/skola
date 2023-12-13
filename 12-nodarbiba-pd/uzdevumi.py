# Dāvis Lektauers, 11.1
# 11.12.2023

# 1. uzdevums - piekļuve vārdnīcu vērtībām;
# Ir dota sekojoša programma. Papildiniet to, lai izvadītu atslēgu un vērtību pāri lielākajai un mazākajai dict1 vērtībai.
# Piemēram, vārdnīcai { 0: 100, 1: 2, 3: 400 } rezultāts būtu - "Lielākā - 3: 400, mazākā 1: 2".
import random
dict1 = {}
for i in range(0, 100):
    dict1.update({i: random.randint(0, 1000)})

largest_val = max(dict1.values())
largest_val_key = list(dict1.keys())[list(dict1.values()).index(largest_val)] # Nav pats tīrākais kods, bet negribās piņķerēties ar cikliem
smallest_val = min(dict1.values())
smallest_val_key = list(dict1.keys())[list(dict1.values()).index(smallest_val)]
print(f"Lielākā - {largest_val_key}: {largest_val}, mazākā - {smallest_val_key}: {smallest_val}")

# 2. uzdevums - vārdnīcu izveide
# Ir doti divi saraksti. Izveidojiet vārdnīcu (izmantojot ciklus) no šiem sarakstiem, kur atslēgas ir šo sarakstu individuālu vērtību kombinācijas un vērtības ir gadījumskaitļi 1-10.
# Piemēram, ja 
# a = [ 'a', 'b' ] un b = [ 'c', 'd' ], tad
# vardnica = { 'ac': 10, 'ad': 4, 'bc': 6, 'bd': 1 }
""" import random
a = [ 'a', 'b', 'e', 'f' ]
b = [ 'c', 'g', 'h', 'z' ]
vardnica = {}

for ai in a:
    for bi in b:
        key = ai + bi
        vardnica[key] = random.randint(1, 10)
print(vardnica) """

# 3. uzdevums - vērtību dzēšana
# Ir dota sekojoša programma, kas izveido vārdnīcu dict1. Papildiniet šo programmu tā,
# lai šī programma izveidotu _izdzēstu_ vērtības no dict1, kas ir mazākas par 500.
# Nedrīkst veidot atsevišķu vārdnīcu vai papildus mainīgos - visām darbībām jānotiek ar dict1.
""" import random
dict1 = {}
for i in range(0, 100):
    dict1.update({i: random.randint(0, 1000)})

i = 0
while True:
    if list(dict1.values())[i] < 500:
        dict1.pop(list(dict1.keys())[i])
    else:
        i += 1
    if i >= len(dict1):
        break
print(dict1) """

# 4. uzdevums - vērtību ielāde un apstrāde
# Ir dots fails "uzdevums.json". Šis fails satur vārdnīcu json formātā. Atveriet šo failu un izvadiet šīs vārdnīcas vērtības formātā 
# "Atslēga: <atslēga>, Vērtība: <vērtība>" (ieskaitot leņķa iekavas <>).
""" import json

with open("uzdevums.json", "r") as f:
    data = json.load(f)
    for i in data:
        print(f"Atslēga: <{i}>, Vērtība: <{data[i]}>") """

# 5. uzdevums - vērtību glabāšana
# Izveidot programmu, kas nodrošina vairāku (! - saraksts) cilvēku informācijas ievadi - vārdu, uzvārdu, vecumu.
# Informāciju par individuālu cilvēku glabāt vārdnīcā ar atslēgām "vards", "uzvards" un "vecums".
# Šīs informācijas izvadi veikt failā ar nosaukumu "dati.json".
""" import json

data = []
while True:
    inp = input("Ievadiet \"s\", lai saglabātu datus un pārtrauktu programmu, vai \"p\", lai pievienotu jaunu cilvēku: ")
    if inp.lower() == "s":
        break
    elif inp.lower() != "p":
        print("Nezināma komanda!")
        continue

    name = input("Ievadiet cilvēka vārdu: ")
    last_name = input("Ievadiet cilvēka uzvārdu: ")

    # Vecuma ievades validācija
    while not (age := input("Ievadiet cilvēka vecumu: ")).isdigit():
        print(f"\"{age}\" nav pareizi ievadīts vecums, mēģiniet vēlreiz!")
    age = int(age)

    data.append({
        "vards": name,
        "uzvards": last_name,
        "vecums": age
    })

with open("dati.json", "w") as f:
    json.dump(data, f) """