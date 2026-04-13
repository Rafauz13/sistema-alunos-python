# Entrega 1 - Cadastro de alunos e calculo da media individual

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

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

print("\n========== RESULTADO ==========")

for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f" Nota 1: {aluno['nota1']:.1f}")
    print(f" Nota 2: {aluno['nota2']:.1f}")
    print(f" Media: {aluno['media']:.1f}")
