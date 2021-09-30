# 1 - imports
from urllib import response

import pytest
import csv
import requests as requests
from requests import HTTPError

teste_dados_usuarios = [
    ('1', 'João', 'Das Couves', 'couves@jardim.com.br'),
    ('2', 'Maria', 'Solene', 'solene@jardim.com.br'),
    ('3', 'Paloma', 'Ganbu', 'ganbu@jardim.com.br'),
    ('4', 'Mirtes', 'Bragança', 'bragan@jardim.com.br'),
    ('5', 'Adolfo', 'Soares', 'soares@jardim.com.br')
]

teste_dados_usuarios_atuais = [
    ('1', 'George', 'Bluth', 'george.bluth@reqres.in'),
    ('2', 'Janet', 'Weaver', 'janet.weaver@reqres.in'),
    ('3', 'Emma', 'Wong', 'emma.wong@reqres.in'),
    ('4', 'Eve', 'Holt', 'eve.holt@reqres.in'),
    ('5', 'Charles', 'Morris', 'charles.morris@reqres.in')
]
# CRUD/ ICAE
# Aplicações            APIs            Português
# Create                Post            Criar / Publicar
# Reach / Research      Get             Consultar / Pegar
# Update                Put             Atualizar
# Delete                Delete          Excluir


@pytest.mark.parametrize('id, nome, sobrenome, email', teste_dados_usuarios)
def testar_dados_usuarios(id, nome, sobrenome, email): # função que testa algo
    try:
        requests.get(f'httpd://reqres.in/api/user/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - e-mail: {email_obtido}')

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email


    except HTTPError as http_err :
        print(f'Um erro de HTTP foi detectado: {http_err}')
    except Exception as fail:
        print(f'Erro inesperado: {fail}')



# def dados_usuarios(): # função que faz algo -- > Fora do computador
# API
# https://reqres.in/api/users/{id}