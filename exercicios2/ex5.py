def verificar_cpf():
    cpf = input("Digite seu CPF (somente números): ")

    if len(cpf) != 11:
        print("CPF inválido: deve conter exatamente 11 dígitos.")
    elif not cpf.isdigit():
        print("CPF inválido: deve conter apenas números.")
    else:
        print("CPF válido.")
