peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (cm): "))

altura_metros = altura / 100

imc = peso / (altura_metros * altura_metros)

print(f"\nO seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Fora do peso normal")
elif imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")