# 25.09.2023
# Dāvis Lektauers 11.1

import random

num = random.randint(1, 100)
guesses = []

while True:
    inp = input("Ievadiet skaitli: ")
    if not inp.isnumeric():
        print("Tas nav skaitlis!")
        continue
    n = int(inp)

    guesses.append(n)

    if n > num:
        print("Mazāk")
    elif n < num:
        print("Augstāk")
    else:
        break

print("Uzvara!")
print(f"Tu minēji {len(guesses)} reizes: {', '.join(str(i) for i in guesses)}")