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


peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (cm): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"\nO seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")