import requests


def verifica_acessibilidade(url):
    try:
        response = requests.get(url)
        # Verifica se o código de status da resposta é 200 (OK)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


# URL do site que você deseja verificar
url = "http://www.pudim.com.br"

if verifica_acessibilidade(url):
    print(f"O site {url} está acessível.")
else:
    print(f"O site {url} não está acessível.")
