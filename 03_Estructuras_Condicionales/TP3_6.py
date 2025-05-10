#escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
# Se importan las librerias de statics y random
# statics = funciones estadisticas matematicas
#random= numeros aleatorios

numeros_aleatorios = [random.randint (1, 100) for i in range (10)] 

mediana = median (numeros_aleatorios)
media  = mean (numeros_aleatorios)
moda = mode (numeros_aleatorios)

print (numeros_aleatorios)
print (mediana)
print(media)
print(moda)

if media > mediana and mediana > moda:
    print("El sesgo es positivo")
elif media < mediana and mediana > moda:
    print("El sesgo es negativo")
else:
    print ("Sin sesgo")








