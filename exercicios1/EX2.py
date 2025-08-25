#2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.
# Função para exibir a tabuada de um número
def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
num = int(input("Digite um número para ver sua tabuada: "))
mostrar_tabuada(num)
