#7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
# imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = str(input("Ingrese una frase o palabra: "))

ultima_letra = frase [-1]

if ultima_letra == "a" or ultima_letra == "A":
    concatenada= frase + "!"
    print (concatenada)
elif ultima_letra == "e" or ultima_letra == "E":
    concatenada= frase + "!"
    print (concatenada)
elif ultima_letra == "i" or ultima_letra == "I":
    concatenada= frase + "!"
    print (concatenada)
elif ultima_letra == "o" or ultima_letra == "O":
    concatenada= frase + "!"
    print (concatenada)
elif ultima_letra == "u" or ultima_letra == "U":
    concatenada= frase + "!"
    print (concatenada)
else:
    print (frase)
