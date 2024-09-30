###  https://github.com/MRvinyKing/SED-Account-Checker
## Projeto Do github 
# Caso goste deixe uma avaliação lá

import requests, random, string, time

usuario = "seu login (rg1234567sp)" 
senha = "sua senha"
delay = 60 # Atraso em segundos para cada tentativa

def request_block():
    url = "https://sed.educacao.sp.gov.br/Logon/LogOn/"
    cookie = ''.join(random.choices(string.ascii_letters + string.digits, k=24)) # Gera cookies novos 

    headers = {
        "Host": "sed.educacao.sp.gov.br",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": f"ASP.NET_SessionId={cookie}",
    }

    data = {
        "usuario": f"{usuario}",
        "senha": f"{senha}"
    }
    
    response = requests.post(url, headers=headers, data=data)
    print(f"\n{'='*50}")
    print(f"Finger Print: {cookie}")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        try:
            response_json = response.json()
            
            if isinstance(response_json, dict):
                if response_json.get("retorno") == "invalido" and "contador" in response_json:
                    contador = response_json["contador"]
                    print(f"{contador} Tentativas até o bloqueio")
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
            print("error: response is not a valid JSON")
    else:
        print(f"error: status code {response.status_code}")
    print(f"{'='*50}")

while True:
    try:
        request_block()
        print(f"Proxima tentativa: {delay} s")
        time.sleep(delay)
        
    except Exception as e:
        print(f"Erro, Tentando novamente: {e}")
