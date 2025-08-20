peso = float(input("Indique su peso en kilogramos: "))
altura = float(input("Indique su altura en metros"))

IMC = peso / (altura**2)

print (f"Su IMC es: {IMC:.2f}")