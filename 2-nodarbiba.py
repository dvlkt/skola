# 18.09.2023
"""
x = "Teksts"
print(x[4])
print(x[3:5])
print(x[:5])
"""

"""
# Ievade: cilvēka vārds
# Izvade: bez pēdējā burta

print("Sveiks, " + input("Ievadi vārdu: ")[:-1])
"""

"""
y = ["T", "e", "k"]
print(",".join(y))
"""

"""
x = ("123", "456", "789")
print(len(x))
"""

"""
x = True
while True:
    x = False

for i in ("a", "b", "c"):
    print(i)
"""

num_count = int(input("Skaitļu daudzums: "))
nums = []
for i in range(num_count):
    nums.append(int(input(f"Skaitlis #{i+1}: ")))
print(f"Summa: {sum(nums)}")