senha_correta = "senha123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha: ")
    
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Acesso bloqueado.")