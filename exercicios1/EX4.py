#4. Desenvolva um programa que leia uma lista de números e mostre a média deles.
# Função para calcular a média de uma lista de números
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Programa principal
numeros = []

print("Digite os números (digite 'sair' para finalizar):")
while True:
    entrada = input("> ")
    if entrada.lower() == "sair":
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")

# Resultado
media = calcular_media(numeros)
print(f"\nVocê digitou: {numeros}")
print(f"A média dos números é: {media:.2f}")