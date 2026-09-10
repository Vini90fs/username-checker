import requests
from sites import SITES

def check_username(username):
    resultados = []
    for site in SITES:
        nome = list(site.keys())[0]
        url = list(site.values())[0]

        url = url.replace("{username}", username)

        try:
            resposta = requests.get(url, timeout=5)
        except requests.exceptions.RequestException:
            resultado = {
                "site": nome,
                "status": "Erro de conexao",
                "url": url
            }

            resultados.append(resultado)
            continue

        if resposta.status_code == 200:
            resultado = {
                "site": nome,
                "status": "Encontrado",
                "url": url
            }

            resultados.append(resultado)
            
        elif resposta.status_code == 403:
            resultado = {
                "site": nome,
                "status": "Nao foi possivel verificar",
                "url": url
            }

            resultados.append(resultado)

        elif resposta.status_code == 404:
            resultado = {
                "site": nome,
                "status": "Nao encontrado",
                "url": url
            }
            
            resultados.append(resultado)

    return resultados



