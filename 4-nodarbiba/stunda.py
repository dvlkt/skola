def foo(a, b):
    return a+b

def just_print(a):
    print(a)

x = foo(10, 3)
y = just_print("Lol")
print(x)
print(y)

def mult_parameters(*params):
    print(len(params))
print(mult_parameters(1, 2, 3, 4, 5))

def recursive(a):
    print(a)
    if a > 0:
        return recursive(a-1)
    else:
        return
recursive(10)


def rec_fact(n):
    if n == 1:
        return 1
    else:
        return n * rec_fact(n-1)
print(rec_fact(7))

def w_fact(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
print(rec_fact(7))

def k_fun(a, b = 2):
    print(a, b)
k_fun(5)

def static_types(a: int, b: str) -> int:
    print(b)
    return 5 + a
static_types(5, "eeeee")

import ramirent
ramirent.ramirent("ramirent")