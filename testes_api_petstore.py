import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200      # comunicação
    codigo_esperado = 200           	# funcional
    tipo_esperado = 'unknown'       		# fixo como desconhecido
    mensagem_esperada = '12181'     # id do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.put(url=f'{url}/{user}',
                            data=open('json/usuario2.json', 'rb'),
                            headers=headers
                            )
    corpo_da_resposta = resposta.json()
    print(resposta) # Status Code
    print(resposta.status_code) # Status Code
    print(corpo_da_resposta) # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    # Configura
    username = 'lauda' # input / entrada para a consulta
    id_esperado = 12181
    username_esperado = 'lauda'
    email_esperado = 'lauda@iterasys.com.br'
    telefone_esperado = '11999992181'
    user_status_esperado = 0
    status_code_esperado = 200      # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta) # Status Code
    print(resposta.status_code) # Status Code
    print(corpo_da_resposta) # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado

def testar_alterar_usuario():
    # Configura
    user = 'lauda'
    status_code_esperado = 200  # comunicação
    codigo_esperado = 200  # funcional
    tipo_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '12181'  # id do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa

    resposta = requests.put(url=f'{url}/{user}',
                            data=open('json/usuario2.json', 'rb'),
                            headers=headers
                            )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():

    # Configura
    username = 'lauda'  # input / entrada para a consulta
    tipo_esperado = 'unknown'       		# fixo como desconhecido
    status_code_esperado = 200      # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.delete(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta) # Status Code
    print(resposta.status_code) # Status Code
    print(corpo_da_resposta) # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == username

def testar_consultar_usuario_e_extrair_senha(username):
    # Configura
    id_esperado = 12181
    username_esperado = 'lauda'
    email_esperado = 'lauda@iterasys.com.br'
    telefone_esperado = '11999992181'
    user_status_esperado = 0
    status_code_esperado = 200  # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado

    return corpo_da_resposta['password']

def testar_login(username,password):

    # Configura
    status_code_esperado = 200  # comunicação / funcional
    tipo_esperado = 'unknown' # default = desconhecido - padrão da API
    mensagem_esperada = 'logged in user session' # COMEÇO DA MENSAGEM

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/login?username={username}&password={password}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert mensagem_esperada in corpo_da_resposta['message']
    token = corpo_da_resposta['message'].rpartition(':')[-1]

    print(f'token: {token}')
    return token


def testar_orquestracao_consultar_senha_e_realizar_login():

    #vai orquestrar as chamadas de duas funções para atingir o seu objetivo

    # configura
    username = 'lauda'

    # Executa
    password = testar_consultar_usuario_e_extrair_senha(username)
    token = testar_login(username,password)
    print(f'token no maestro: {token}')