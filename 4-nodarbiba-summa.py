def sum(nums):
    result = 0
    for i in nums:
        result += int(i)
    return result

inp = input("Ievadiet skaitļus, atdaliet ar komatiem: ").split(",")
print(f"Summa ir {sum(inp)}")