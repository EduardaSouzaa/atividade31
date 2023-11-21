#Crie um programa que leia dois números e mostre a soma, a
#subtração, a multiplicação e a divisão entre eles

def soma(n1, n2):
    soma = n1 + n2
    print(soma)

def subtração(n1, n2):
    subtração = n1 - n2
    print(subtração)

def multiplicação(n1, n2):
    multiplicação = n1 * n2
    print(multiplicação)

def divisão(n1, n2):
    divisão = n1 / n2
    print(divisão)

n1 = int(input("digite o número 1"))
n2 = int(input("digite o número 2"))

soma(n1, n2)
subtração(n1, n2)
multiplicação(n1 ,n2)
divisão(n1, n2)