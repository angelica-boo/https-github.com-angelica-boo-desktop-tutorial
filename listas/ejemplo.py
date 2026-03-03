def contarVocales(palabra):
    if palabra == "":
        return 0
    
    primera = palabra[0].lower()
    
    if primera in "aeiou":
        return 1 + contarVocales(palabra[1:])
    else:
        return contarVocales(palabra[1:])
    
texto = input("Ingrese una palabra: ")
print("Cantidad de vocales:", contarVocales(texto))