# Entrega 2 - Cadastro de alunos, media individual e estatisticas da turma

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def calcular_media_turma(alunos):
    total = sum(aluno["media"] for aluno in alunos)
    return total / len(alunos)

def aluno_maior_media(alunos):
    return max(alunos, key=lambda a: a["media"])

def aluno_menor_media(alunos):
    return min(alunos, key=lambda a: a["media"])

# Solicitar quantidade de alunos
while True:
    try:
        quantidade = int(input("Informe a quantidade de alunos (entre 2 e 7): "))
        if 2 <= quantidade <= 7:
            break
        else:
            print("Quantidade invalida! Digite um valor entre 2 e 7.")
    except ValueError:
        print("Entrada invalida! Digite um numero inteiro.")

alunos = []

for i in range(quantidade):
    print(f"\n--- Aluno {i + 1} ---")
    nome = input("Nome do aluno: ")

    while True:
        try:
            nota1 = float(input("Nota 1 (0.0 a 10.0): "))
            if 0.0 <= nota1 <= 10.0:
                break
            else:
                print("Nota invalida! Digite um valor entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada invalida! Digite um numero.")

    while True:
        try:
            nota2 = float(input("Nota 2 (0.0 a 10.0): "))
            if 0.0 <= nota2 <= 10.0:
                break
            else:
                print("Nota invalida! Digite um valor entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada invalida! Digite um numero.")

    media = calcular_media(nota1, nota2)

    alunos.append({
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    })

# Resultado individual
print("\n========== RESULTADO INDIVIDUAL ==========")

for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f" Nota 1: {aluno['nota1']:.1f}")
    print(f" Nota 2: {aluno['nota2']:.1f}")
    print(f" Media: {aluno['media']:.1f}")

# Estatisticas da turma
media_turma = calcular_media_turma(alunos)
maior = aluno_maior_media(alunos)
menor = aluno_menor_media(alunos)

print("\n========== ESTATISTICAS DA TURMA ==========")
print(f"A media da turma e: {media_turma:.2f}")
print(f"A turma tem {len(alunos)} alunos")
print(f"O aluno que obteve a maior media foi {maior['nome']} com {maior['media']:.2f}")
print(f"O aluno que obteve a menor media foi {menor['nome']} com {menor['media']:.2f}")