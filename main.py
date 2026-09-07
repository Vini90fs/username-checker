from sites import SITES

print("================================")
print("        USERNAME CHECKER")
print("================================")

username = input("Digite o username: ")

print()
print("Username pesquisado:", username)

for site in SITES:
    print(site)