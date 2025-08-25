def soma_com_contagem(n):
    soma = 0
    operacoes = 0

    for i in range(1, n + 1):
        soma += i
        operacoes += 1  # cada soma é uma operação básica

    formula = n * (n + 1) // 2

    print(f"Soma calculada com laço: {soma}")
    print(f"Número de operações básicas (somas): {operacoes}")
    print(f"Soma pela fórmula matemática: {formula}")
    