from checker import check_username

username = input("Digite o username: ")

print("Username:", username)

resultados = check_username(username)

for resultado in resultados:
    print(resultado)