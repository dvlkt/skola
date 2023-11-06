# Dāvis Lektauers, 11.1
# 06.11.2023
# 2. variants - karātavas

import random

word_bank = [
    "lampa",
    "himalaji"
    "zaļums",
    "lasīšana",
    "sabiedrība",
    "blokshēma"]

lives = 5
word = random.choice(word_bank)
guessed_letters = []

while True:
    # Paslēpj neuzminētos burtus
    hidden_word = ""
    for i in word:
        if i in guessed_letters:
            hidden_word += i
        else:
            hidden_word += "_"
    print(f"{hidden_word}   Dzīvības: {lives}")
    
    # Pārbauda, vai guess ir vienu rakstzīmi garš un vai tas ir burts
    while len(guess := input("Miniet burtu: ")) != 1 or not guess.isalpha():
        print("Jāievada viens burts!")
    guessed_letters.append(guess.lower())

    # Pārbauda, vai tāds burts vispār ir dotajā vārdā
    if not guess in word:
        print("Vārdā nav tāda burta!")
        lives -= 1
    
    print()

    # Zaudēšana
    if lives <= 0:
        print("Zaudējāt")
        break
    
    # Uzvarēšana - pāŗbauda, vai visi burti ir uzminēti
    has_won = True
    for i in word:
        if not i in guessed_letters:
            has_won = False
            break
    if has_won:
        print("Uzvarējāt")
        break

print(f"Pareizā atbilde bija \"{word}\"")