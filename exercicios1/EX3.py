#3. Crie uma função que verifique se um número é primo.
# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Programa principal
num = int(input("Digite um número para verificar se é primo: "))

# Resultado
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")