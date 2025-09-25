cnumero = 0

for i in range (1,101):
    numero = int(input(f"Ingrese su numero nº{i} : "))
    cnumero = cnumero + numero

media = cnumero/i
print("La media es:", media)