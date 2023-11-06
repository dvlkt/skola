# Dāvis Lektauers 11.1
# 16.10.2023

year = int(input("Ievadiet gadu: "))
if year % 400 == 0:
    print("Tas ir garais gads")
elif year % 100 == 0:
    print("Tas nav garais gads")
elif year % 4 == 0:
    print("Tas ir garais gads")
else:
    print("Tas nav garais gads")