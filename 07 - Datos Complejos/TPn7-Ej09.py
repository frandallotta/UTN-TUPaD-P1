agenda = {
    ("lunes", "10:00"): "Clases",
    ("martes", "21:00"): "Futbol",
    ("miercoles", "09:00"): "Entrenamiento",
    ("viernes", "22:00"): "Cena con amigos"
}

def consultar_evento(dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"\nEl evento programado es: {agenda[clave]}"
    else:
        return "\nNo hay ningún evento programado en ese día y hora."


dia_consulta = input("\nIngrese el día: ")
hora_consulta = input("Ingrese la hora (HH:MM): ")

resultado = consultar_evento(dia_consulta, hora_consulta)
print(resultado)