# 1 - imports
import json

import pytest
import csv

import requests
from requests import HTTPError

teste_dados_novos_usuarios = [
    (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),         # usuário 1
    (2, 'Agatha', 'Christie','agatha@iterasys.com.br')     # usuario 2
]

teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),   # usuário 1
    (2, 'Janet', 'Weaver','janet.weaver@reqres.in')     # usuario 2
]

# CRUD / ICAE
# Aplicações        APIs        Português
# Create            Post        Incluir / Publicar
# Reach / Research  Get         Consultar / Pegar
# Update            Put         Atualizar
# Delete            Delete      Excluir

@pytest.mark.parametrize('id,nome,sobrenome,email', teste_dados_usuarios_atuais) # os campos chaves id,nome,sobrenome,email
def testar_dados_usuarios(id,nome,sobrenome,email): # função que testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}') # get consultamos o edereço informado.
        jsonResponse = response.json() # () não chamamos um dado em expecifico, quando não atribui valor dentro dos parenteses, estou dizendo que desejo receber o arquivo completo.
        id_obtido = jsonResponse['data']['id'] # chama ID
        nome_obtido = jsonResponse['data']['first_name'] # chama primeiro nome
        sobrenome_obtido = jsonResponse['data']['last_name'] # chama ultimo nome
        email_obtido = jsonResponse['data']['email'] # chama email
        # consulte https://reqres.in/
                        #{
                         #   "data": {
                          #      "id": 2,
                           #     "email": "janet.weaver@reqres.in",
                            #    "first_name": "Janet",
                             #   "last_name": "Weaver",
                              #  "avatar": "https://reqres.in/img/faces/2-image.jpg"
                            #},
                            #"support": {
                            #   "url": "https://reqres.in/#support-heading",
                            #  "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
                            #}
                        #}

        print(f'id: {id_obtido} \n nome: {nome_obtido} \n sobrenome: {sobrenome_obtido} \n email: {email_obtido}')
        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')
        print('id:{} \n nome:{} \n sobrenome:{} \n email:{}'.format(id_obtido, nome_obtido, sobrenome_obtido, email_obtido))
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_fail : # Para o ISTQB, descobriu rodando é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:        # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')


#função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users/{id}

# Leitor do Arquivo CSV
def ler_dados_do_csv():
    teste_dados_csv = [] # os [] vazio representa uma lista vazia que sera testada.
    nome_arquivo = 'usuarios.csv' # aponta a direção do arquivo que contem os dados
    try:  # tentar
        with open(nome_arquivo,newline='') as csvfile: # como, abrir a(rquivo, nova linha em branco), e declara um "apelido" para o arquivo CSV = csvfile
            dados = csv.reader(csvfile,delimiter=',') # reader para fazer a leitura do arquivo, (declaro o nome do arquivo e wlwmwnto dwlimitador ",")
            next(dados) # crio um looping retornando a linha de cima novamente
            for linha in dados: # Transformo meus dados em linhas
                teste_dados_csv.append(linha) # declaro com append de onde vem os dados para ser considerado pelo def testes_dados_csv
        return teste_dados_csv # retorno resultado de teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}') # utilizar o f fora das 'aspas' para incluir variaveis dentro de {chaves} para interagir com o texto do print
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id,nome,sobrenome,email', ler_dados_do_csv() ) # os campos chaves id,nome,sobrenome,email
def testar_dados_usuarios_csv(id,nome,sobrenome,email): # função que testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}') # get consultamos o edereço informado.
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'id: {id_obtido} \n nome: {nome_obtido} \n sobrenome: {sobrenome_obtido} \n email: {email_obtido}') # Exemplo 1  para pular linha com 'f' e \n
        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}') # Exemplo 2 de para pular linha com 'f' e '-'
        print('id:{} \n nome:{} \n sobrenome:{} \n email:{}'.format(id_obtido, nome_obtido, sobrenome_obtido, email_obtido)) # Exemplo 3 de \n para pular a linha
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == int(id)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_fail : # Para o ISTQB, descobriu rodando é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:        # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')