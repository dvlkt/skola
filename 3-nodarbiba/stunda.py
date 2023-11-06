# 25.09.2023

# Izvadīt skaitļus 1-10, izlaist 4 un 6
for i in range(0, 10+1):
    if i != 4 and i != 6:
        print(i)

# Izvadīt katru otro skaitli no arr
arr = [123, 456, 678, 895]
print(arr[::2])

# FizzBuzz
for i in range(0, 100+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Programma ar šādu izvadi:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(5+1):
    for o in range(1, i+1):
        print(str(o) + " ", end="")
    print("")