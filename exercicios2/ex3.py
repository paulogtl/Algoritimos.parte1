def estatisticas_notas():
    notas = []
    qtd_alunos = int(input("Quantos alunos há na turma? "))

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)

    media = sum(notas) / qtd_alunos
    maior = max(notas)
    menor = min(notas)
    acima_da_media = [nota for nota in notas if nota > media]
    percentual_acima = (len(acima_da_media) / qtd_alunos) * 100

    print(f"\n📊 Estatísticas da Turma:")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Percentual de alunos acima da média: {percentual_acima:.1f}%")