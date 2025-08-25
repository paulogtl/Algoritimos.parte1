#1. Faça um programa que leia dois números e mostre qual é o maior.
# Função para comparar dois números
def mostrar_maior(num1, num2):
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Os dois números são iguais.")

# Programa principal
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamada da função
mostrar_maior(numero1, numero2)