hemisferio = input("Ingrese el hemisferio (Sur/Norte): ").lower()
mes = int(input("Ingrese el numero de mes (1-12): "))
dia = int(input("Ingrese el numero de dia (1-31): "))

if ( (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20) ):
    hemisferio_norte = "Invierno"
    hemisferio_sur = "Verano"
elif ( (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20) ):
    hemisferio_norte = "Primavera"
    hemisferio_sur = "Otoño"
elif ( (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20) ):
    hemisferio_norte = "Verano"
    hemisferio_sur = "Invierno"
elif ( (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20) ):
    hemisferio_norte = "Otoño"
    hemisferio_sur = "Primavera"
else:
    hemisferio_norte = hemisferio_sur = "Fecha inválida"

if hemisferio == "norte":
    print("Usted se encuentra en:", hemisferio_norte)
elif hemisferio == "sur":
    print("Usted se encuentra en:", hemisferio_sur)
else:
    print("Hemisferio inválido")