import requests
from sites import SITES

def interpretar_status(status_code):
    if status_code == 200:
        return "Encontrado"

    elif status_code == 403:
        return "Nao foi possivel verificar"

    elif status_code == 404:
        return "Nao encontrado"

    else:
        return f"Erro HTTP {status_code}"

def check_username(username):
    resultados = []
    for site in SITES:
        nome = site["nome"]
        url = site["url"]

        url = url.replace("{username}", username)

        try:
            resposta = requests.get(url, timeout=5)

            status = interpretar_status(resposta.status_code)

            resultado = {
                "site": nome,
                "status": status,
                "url": url
            }

            resultados.append(resultado)

        except requests.exceptions.RequestException:
            resultado = {
                "site": nome,
                "status": "Erro de conexao",
                "url": url
            }

            resultados.append(resultado)
            continue

    return resultados



