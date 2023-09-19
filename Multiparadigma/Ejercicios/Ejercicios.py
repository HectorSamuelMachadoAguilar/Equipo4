#Bucles
#Escribe un programa que pregunte una frase y una letra, y muestre un mensaje indicando el número de veces que aparece la letra
veces = 0
frase = input("Dime una frase: ")
letra = input("Dime una letra: ")
for l in frase:
    if letra == l:
        veces+=1
print(f'La letra aparece {veces} veces en la frase')

#Cadenas
#

#Clases
#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
#El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
#-Un constructor, donde los datos pueden estar vacíos.
#-Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, solo ingresando o retirando dinero.
#-mostrar(): Muestra los datos de la cuenta.
#-ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#-retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
#
#Definir ahora una "Cuenta Joven", crear una nueva clase CuantaJoven que deriva de la anterior. 
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de "Cuenta Joven" y la bonificación de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.

#Una pizzería vende pizzas vegetarianas y no vegetarianas y aparece una lista de ingredientes vegetarianos y no vegetarianos
#Los ingredientes vegetarianos son: pimiento y tofu
#ingredientes no vegetarianos son: pepperoni, jamon y salami
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
#En funcion a su respuesta, mostrar los ingredientes. Solo se puede pedir un ingrediente, además de la mozzarella y el tomate que está en todas las pizzas
#Al final mostrar un mensaje con todos los ingredientes de la pizza y el tipo de pizza

#Modulos
#Generar 3 archivos, el primero llamado exportador, el segundo llamado importador y el tercero llamado pruebas
#Y en el archivo exportador colocar los siguientes métodos: Matrices a diccionario, tuplas a matrices, set a listas
#El archivo importador diccionario a matriz, listas a set, matriz a tuplas
#Y el archivo de pruebas va a mandar a llamar a los 2 modulos

#Diccionario
#Escribir un programa que escriba en un diccionario los precios de las frutas de la siguiente manera:
#En la primer columna es fruta y la segunda es precio
#De frutas es plátano, manzana, pera y naranja
#En la segunda columna es 1.35, 0.80, 0.85 y 0.7
#Guardar el nombre de las frutas en mayusculas
#Preguntar al usuario por una fruta y el número de kilos
#Mostrar en pantalla el total y si la fruta no está en el diccionario, mostrar un mensaje de ello

#Listas y tuplas
#Escribir una lista que almacene las siguientes matrices:
# A= [[1,2,3]]  B=[[-1,0]]
#    [[4,5,6]]    [[0,1]]
#                 [[1,1]]
#Mostrar en pantalla su producto almacenado en tuplas

#Matrices
#En una matriz de 5x4 pedir al usuario los valores
#En una segunda matriz de 5x4 guardar:
#Si es multiplo de 3 guardar un 2
#Si el numero es multiplo de 5 guardar un 3
#Y un 4 si es un multiplo de 3 y 5 a la vez, si no se cumple ninguna de las anteriores, guardar un 0

#Tipos de datos
#Una juguetería tiene mucho exito en 2 de sus productos: payasos y muñecas. 
#Se suele hacer la venta por correo y la empresa de logistica les cobra por peso de cada paquete
#Así que deben calcular el peso de los payasos y muñecas. Cada payaso pesa 112 gramos y cada muñeca 75 gramos
#Escriba un programa que lea el número de payasos y muñecas vendidas en el último periodo
#Calcule el peso total del paquete y el precio total si por cada 100 gramos de payaso se cobra 3 pesos
#Y por cada 100 gramos de muñeca 2 pesos

#Archivos
#En base al siguiente .scv realiazar lo siguiente crear una funcion que cree un diccionario ordenado por nombre
#Crear otra funcion que ordene por numero de control
#Una funcion que ordene por calificacion