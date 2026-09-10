from checker import check_username

username = input("Digite o username: ")

print("Username:", username)

resultados = check_username(username)

for resultado in resultados:
    if(resultado["status"] == "Encontrado"):
        print(resultado["site"], ">", resultado["status"], ">", resultado["url"])

    else:
        print(resultado["site"], ">", resultado["status"])