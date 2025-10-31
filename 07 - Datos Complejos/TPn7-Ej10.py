original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Peru": "Lima"
}

invertido = {capital: pais for pais, capital in original.items()}

print("\nDiccionario original:\n", original)
print("\nDiccionario invertido:\n", invertido)