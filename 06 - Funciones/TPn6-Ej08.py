def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {resultado:.2f}")