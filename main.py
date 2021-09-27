# imports - bibliotecas
import pytest
# 2 - class - classes

# 3 - definitions - definições = métodos e funções

# Cada "def" é um metódo
def print_hi(name):
    print(f'Oi, {name}')

def somar (num1, num2):
    return num1 + num2

def subtrair  (num1, num2):
    return num1 - num2

def dividir(num1, num2):
    if num1 != 0:
        return num1 / num2
    else:
        return "Não dividir número igual a 0"

def multiplicar  (num1, num2):
    return num1 * num2

#testes unitários / Testes de UNidades

#testes da função somar
@pytest.mark.parametrize('num1, num2, resultado',[
    #valores
    (5, 4, 9),# testes 1
    (3, 2, 5),# testes 2
    (10, 6, 16),# testes 3
])
def test_somar(num1, num2, resultado):
    assert somar(num1, num2) == resultado
'''
def test_somar():
    # 1 - Configura / Prepara
    num1 = 8 # input / entrada
    num2 = 5 # input / entrada
    resultado_esrepado = 13 # output / saida

    # 2 - Executa
    resultado_atual = somar(num1,num2)

    # 3 - Check / Valida
    assert resultado_atual == resultado_esrepado

#o mesmo teste só que resumido
def test_somar_compacto():
    assert somar(8,5) == 13

def test_somar_resultado_negativo():
    assert somar(-1000,-2000) == -3000

def teste_subtrair():
    assert subtrair(4,5) == -1

def teste_multiplicar():
    assert multiplicar(3,7) == 21

def testes_dividir():
    assert dividir(8,4) == 2
'''

if __name__ == '__main__':
    print_hi('Manoel')

    resultado = somar(4, 2)
    print(f'O resultado de somar é: {resultado}')

    resultado = subtrair(14, 23)
    print(f'O resultado de subtrair é: {resultado}')

    resultado = dividir(0, 782)
    print(f'O resultado de dividir é: {resultado}')

    resultado = multiplicar(14, 211)
    print(f'O resultado de multiplicar é: {resultado}')



