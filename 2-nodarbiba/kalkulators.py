# Dāvis Lektauers, 18.09.2023

# Skaitļu ievadīšana
nums = []
while True:
    inp = input("Ievadiet skaitli vai 'q', lai pabeigtu skaitļu ievadi: ")
    if inp == "q":
        if len(nums) < 2:
            print("Vēl nav ievadīti vismaz 2 skaitļi!")
        else:
            break
    else:
        nums.append(float(inp))

# Darbības ievadīšana
while True: # Cikls, lai pārliecinātos, ka ievadītā darbība ir pareiza
    op = input("Ievadiet darbību (+, -, *, / vai ^): ")
    if op in ("+", "-", "*", "/", "^"):
        break
    else:
        print("Šāda darbība nav pieejama")

# Aprēķināšana
result = 0
for i in range(len(nums)):
    if i == 0:
        result = nums[i]
        continue

    if op == "+":
        result += nums[i]
    elif op == "-":
        result -= nums[i]
    elif op == "*":
        result = result * nums[i]
    elif op == "/":
        result = result / nums[i]
    elif op == "^":
        result = result ** nums[i]

print(f"Rezultāts ir {round(result, 5)}")