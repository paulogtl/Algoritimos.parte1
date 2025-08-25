def busca_linear(nomes, nome_procurado):
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_procurado.lower():
            return i  # Retorna a posição (índice) onde o nome foi encontrado
    return -1  # Retorna -1 se não encontrar

# Exemplo de uso
lista_de_nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
nome = input("Digite o nome que deseja buscar: ")

posicao = busca_linear(lista_de_nomes, nome)

if posicao != -1:
    print(f"✅ Nome encontrado na posição {posicao}.")
else:
    print("❌ Nome não encontrado.")