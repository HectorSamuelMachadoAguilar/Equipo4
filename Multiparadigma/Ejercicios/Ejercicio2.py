# #Dividir cierto entero n entre otro entero m hasta que n=1 obteniendo una secuencia de números
# #Cada número de esa secuencia se almacena en una lista. La secuencia debe cumplir hasta llegar a n=1. 
# #Si n=1 imprimir la secuencia entera, de lo contrario imprimir "Secuencia invalida"
# try:
#     ListaNumeros = []
#     n = int(input("Introduzca en dividendo: "))
#     m = int(input("Introduzca en divisor: "))
    
#     if m == 1:
#         print(n)
#     else:
#         while n!=1:
#             ListaNumeros.append(int(n))
#             n = n/m
# except ZeroDivisionError:
#     print("No se puede dividir entre 0")
# except ValueError:
#     print("Introdujo un caracter invalido o un número con decimal")
# except:
#     print("Ocurrió un error")
# else:    
#     if n==1:
#         ListaNumeros.append(int(n))
#         print("\nSecuencia:")
#         for obj in ListaNumeros:
#             print(obj)
#     elif m==1:
#         print("Secuencia correcta")
#     else:
#         print("Secuencia equivocada")

#Una chocolatería lanzará un nuevo producto, el cual viene presentado en barras de n segmentos.
#Las barras solo vienen en tamaños que son potencia de 2.
#Realizar un programa para realizar una prueba de calidad de dicho producto, pero para ello debes de probar al menos m segmentos
#El problema es que la barra solo se puede partir a la mitad, dicho programa determinará el número de veces que quebrarás la barra para obtener n
#segmentos exactamente. La salida será el tamaño minimo de barra que se tendrá que pedir para probar los m segmentos
#Y el segundo número es el número de veces que se tendrá que partir la barra

# Entrada = int(input("introduzca en número de segmentos que tiene la barra a probar: "))
# Potencia = 0
# VecesPartido = 0

# while (2**Potencia) < Entrada:
#     Potencia += 1

# Segmento = 2**Potencia
# Aux = 0

# if Segmento != Entrada:
#     while Aux != Entrada:
#         Segmento = Segmento / 2
#         VecesPartido+=1
#         Aux += Segmento
#         if Aux > Entrada:
#             Aux -= Segmento
#             Segmento = Segmento / 2
#             VecesPartido+=1
#             Aux += Segmento
#     print(f"Salida: {2**Potencia},{VecesPartido}")
# else:
#     print(f"Salida: {2**Potencia},{VecesPartido}")

# Listas = [
#     [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10], 
#     [11,12,13,14,15,16,17,18,19,20], 
#     [21,22,23,24,25,26,27,28,29,30], 
#     [31,32,33,34,35,36,37,38,39,40], 
#     [41,42,43,44,45,46,47,48,49,50], 
#     [51,52,53,54,55,56,57,58,59,60], 
#     [61,62,63,64,65,66,67,68,69,70], 
#     [71,72,73,74,75,76,77,78,79,80], 
#     [81,82,83,84,85,86,87,88,89,90], 
#     [91,92,93,94,95,96,97,98,99,100]
#     ]

# def Numero(Fila):
#     Suma = 0
#     Columna = 0
#     if Fila >= 0 and Fila <= 9:
#         while Columna < 10:
#             Suma += Listas[Columna][Fila]
#             Columna+=1
#     elif Fila == 10:
#         while Columna < 10:
#             Suma += Listas[Columna][Columna]
#             Columna+=1
#         while Columna > 0:
#             Columna-=1
#             Suma += Listas[Columna][Columna]
#     else:
#         print("Valor no válido")
#     return Suma
# try:
#     Fila = int(input("Dame un número del 0 al 10: "))
#     print(Numero(Fila))
# except:
#     print("\nDebes introducir un número del 0 al 10")

import random
def Funcion(NumeroF,ListaF):
    Matriz = [[0 for _ in range(NumeroF)] for _ in range(NumeroF)]
    for n in range(NumeroF):
        Matriz[n][n] = ListaF[n]
        Matriz[n][NumeroF - 1 - n] = ListaF[n]
    print(Matriz)

Numero = int(input("Dame un número: "))
if 4 <= Numero <= 100:
    Lista = [random.randint(0,100) for _ in range(Numero)]
    Funcion(Numero,Lista)
else:
    print("Valor no válido")