def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
   
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))     
print(contar_digito(123456, 7))
