# 11.09.2023

print("11.1")

"""
n = input("Ievade: ")
if n == "sveiki":
    print("sveiki")
else:
    print(n)
"""

import random
num = random.randint(1, 100)
while (n := int(input("Skaitlis: "))) != num:
    if n < num:
        print("Lielāk")
    else:
        print("Mazāk")
print("Malacītis")