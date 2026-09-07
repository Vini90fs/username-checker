import requests
from sites import SITES

def check_username(username):
    resultados = []
    for site in SITES:
        nome = list(site.keys())[0]
        url = list(site.values())[0]

        url = url.replace("{username}", username)

        resposta = requests.get(url)

        if resposta.status_code == 200:
            resultados.append(nome + " > Encontrado")
            
        elif resposta.status_code == 403:
            resultados.append(nome + " > Nao foi possivel verificar")

        elif resposta.status_code == 404:
            resultados.append(nome + " > Nao encontrado")

    return resultados



