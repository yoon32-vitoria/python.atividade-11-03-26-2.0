
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

aluno = {
    'nome': nome,
    'nota1': nota1,
    'nota2': nota2
}

media = (nota1 + nota2) / 2


aluno['media'] = media

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

if media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nSituação do aluno: {situacao}")
