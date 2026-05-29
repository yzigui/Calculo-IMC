def calcular_imc(peso: float, altura_cm: float) -> float:
    altura_metros = altura_cm / 100
    imc = peso / (altura_metros * altura_metros)
    return imc


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def classificacao_mais_frequente(classificacoes: list) -> str:
    mais_frequente = classificacoes[0]

    for classificacao in classificacoes:
        if classificacoes.count(classificacao) > classificacoes.count(mais_frequente):
            mais_frequente = classificacao

    return mais_frequente


imcs = []
classificacoes = []

while True:
    try:
        peso = float(input("Digite o seu peso (kg): "))
        altura = float(input("Digite a sua altura (cm): "))

        if peso <= 0 or altura <= 0:
            print("Erro: o peso e a altura devem ser maiores que zero.")
            continue

        if peso < 1 or peso > 1000:
            print("Erro: peso inválido.")
            continue

        if altura < 30 or altura > 250:
            print("Erro: digite uma altura realista em centímetros.")
            continue

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        imcs.append(imc)
        classificacoes.append(classificacao)

        print(f"\nO seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

        continuar = input("\nDeseja realizar outra consulta? (s/n): ")

        if continuar.lower() != "s":
            break

    except ValueError:
        print("Erro: digite apenas valores numéricos.")

if len(imcs) > 0:
    total_consultas = len(imcs)
    media_imc = sum(imcs) / total_consultas
    mais_frequente = classificacao_mais_frequente(classificacoes)

    print("\nResumo das consultas")
    print("----------------------")
    print(f"Total de consultas realizadas: {total_consultas}")
    print(f"Média dos IMC calculados: {media_imc:.2f}")
    print(f"Classificação mais frequente: {mais_frequente}")
else:
    print("\nNenhuma consulta foi realizada.")