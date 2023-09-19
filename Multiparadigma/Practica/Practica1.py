#1 Funciones con n parámetros
#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
#producto total y su suma total.

#def SumaYProducto(*numeros):
    #suma = 0
    #producto = 1
    #for i in numeros:
        #suma += i
        #producto *= i	
    #print(f'La suma total es: {suma} y el producto total es: {producto}')

#SumaYProducto(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

#2 Manejo y manipulación de elementos de una lista
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
#posiciones múltiplos de 2, y muestre por pantalla la lista resultante.

#lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Posicion = len(lista)-1
#while(Posicion > 0):
    #if ((Posicion % 2) == 0):
        #lista.pop(Posicion)
        #Posicion -= 2
    #else:
        #Posicion -= 1
#print(lista)

#3 Entrada de datos y manipulación.
#Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
#manera inversa letra por letra intercalando una letra minuscula a una mayuscula ejemplo Luis : L u I s

#nombre = input("Dime tu nombre completo: ")
#invertido = ""
#Mayuscula = True
#for i in nombre:
    #if i.isalpha():
        #if Mayuscula == True:
            #invertido += i.upper()
            #Mayuscula = False
        #else:
            #invertido += i.lower()
            #Mayuscula = True
    #else:
        #invertido += i
#print(invertido[::-1])


#4 Entrada de datos y estructuración.
#Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
#las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
#“{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de
#todas las materias 

#reticula = { }
#totalCreditos = 0
#lista = [ ]
#condicional = 1
#while (condicional == 1):
    #materia = input("Introduce tu materia preferida: ")
    #creditos = input("introduce los créditos de la materia: ")
    #reticula[materia] = creditos
    #condicional = int(input("Gusta introducir otra materia? [Si=1][No=0]: "))
#for x in reticula:
    #print(f"\n{x} tiene {reticula[x]} creditos")
    #totalCreditos += int(reticula[x])
    #lista.append(x)
#print(f"\nEl total de créditos es: {totalCreditos}. \nLas materias son: {lista}")

#5 Manejo de información
#Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
#“{valor}”: “{llave}”

#def LlaveValor(**kwargs):
    #for llave,valor in kwargs.items():
        #print(f"{llave}: {valor}")

#LlaveValor(Nombre='Héctor', Apellido='Machado', Edad=21)

#6 Razonamiento y prueba de código
#Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
#condicionales, máximo 5 líneas de código.

#ListaNumeros=['Cero','Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez','Once','Doce','Trece','Catorce','Quince','Diesiseis','Diesisiete','Diesiocho','Diesinueve','Veinte']
#numero = int(input("Introduce un número: "))
#print(f"El número {numero} en letra es {ListaNumeros[numero]}")

#7 Formateo y conversiones
#Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
#YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# #del día de hoy en el formato seleccionado.

# #from datetime import date
# #from datetime import datetime
# #opcion = int(input("Selecciona una opcion: \n1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY \nRespuesta: "))
# #fecha=datetime.now()
# #if opcion == 1:
#     #print(f'{date.today():%Y-%m-%d}')
# #elif opcion == 2:
#     #print(f'{date.today():%d-%m-%Y}')
# #else:
#     #print("Opción no válida")

# #8 Resumen y multi-solución
# #8.1.-Definir una clase usuario que contenga como atributos: Usuario, Contraseña, Rol, Nombre, CURP, Ciudad

# class Usuario:
# 	def __init__(self,usuario,contraseña,nombre,curp,ciudad,rol="cliente") -> None:
# 		self._usuario=usuario
# 		self._contraseña=contraseña
# 		self._nombre=nombre
# 		self._curp=curp
# 		self._ciudad=ciudad
# 		self._rol=rol
# 	def __str__(self) -> str:
# 		return f"\nUsuario: {self._usuario} \nContraseña: {self._contraseña} \nNombre: {self._nombre} \nCURP: {self._curp} \nCiudad: {self._ciudad} \nRol: {self._rol} \n"


# #8.2.-Realizar un programa que contenga el siguiente menú 1.- Registro, 2.- Inicio de sesión, 3.- Salida
# #La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase
# #exceptuando el atributo Rol que por defecto será rol cliente, no se permitirán usuarios con CURP
# #repetido en caso de mostrar mensaje de “El usuario ya existe”
# #La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas desplegar
# #en pantalla la información del usuario de lo contrario mostrar mensaje de “datos incorrectos“

# # ListaUsuarios = []
# # opcion = 0
# # while opcion == 0:
# #     opcion = int(input("Seleccione una opción: \n1.-Registro \n2.-Inicio de sesión \n3.- Salida \nRespuesta: "))
# #     if opcion == 1:
# #         usuario = input("\nIntroduzca su usuario: ")
# #         contraseña = input("Introduzca su contraseña: ")
# #         nombre = input("Introduzca su nombre: ")
# #         curp = input("Introduzca su CURP: ")
# #         ciudad = input("Introduzca su ciudad: ")
# #         if ListaUsuarios == []:
# #              miUsuario=Usuario(usuario,contraseña,nombre,curp,ciudad)
# #              ListaUsuarios.append(miUsuario)
# #              print("\nUsuario registrado\n")
# #              opcion = 0
# #         else:
# #             for obj in ListaUsuarios:
# #                 if obj._curp == curp:
# #                       print("\nEl usuario ya existe\n")
# #                       opcion = 0
# #                       break
# #                 else:
# #                     miUsuario=Usuario(usuario,contraseña,nombre,curp,ciudad)
# #                     ListaUsuarios.append(miUsuario)
# #                     print("\nUsuario registrado\n")
# #                     opcion = 0
# #     elif opcion == 2:
# #         usuario = input("\nIntroduzca su usuario: ")
# #         contraseña = input("Introduzca su contraseña: ")
# #         if ListaUsuarios == []:
# #              print("\nNo hay usuarios registrados\n")
# #              opcion = 0
# #         else:
# #             for obj in ListaUsuarios:
# #                 if obj._usuario == usuario and obj._contraseña == contraseña:
# #                       print(obj+"\n")
# #                       opcion = 0
# #                       break
# #                 else:
# #                     print("\nEl usuario no existe\n")
# #                     opcion = 0
# #     elif opcion == 3:
# #          break
# #     else:
# #         print("\nOpción no válida\n")
# #         opcion = 0
# # print("\nHasta luego!")

# #8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la
# #información de todos los usuarios registrados al momento.

# ListaUsuarios = []
# opcion = 0

# miUsuario=Usuario("HectorS","123","Hector","MAAH","Nvo. Laredo","administrador")
# ListaUsuarios.append(miUsuario)

# while opcion == 0:
#     opcion = int(input("Seleccione una opción: \n1.-Registro \n2.-Inicio de sesión \n3.- Salida \nRespuesta: "))
#     if opcion == 1:
#         usuario = input("\nIntroduzca su usuario: ")
#         contraseña = input("Introduzca su contraseña: ")
#         nombre = input("Introduzca su nombre: ")
#         curp = input("Introduzca su CURP: ")
#         ciudad = input("Introduzca su ciudad: ")
#         if ListaUsuarios == []:
#              miUsuario=Usuario(usuario,contraseña,nombre,curp,ciudad)
#              ListaUsuarios.append(miUsuario)
#              print("\nUsuario registrado\n")
#              opcion = 0
#         else:
#             for obj in ListaUsuarios:
#                 if obj._curp == curp:
#                       print("\nEl usuario ya existe\n")
#                       opcion = 0
#                       break
#                 else:
#                     miUsuario=Usuario(usuario,contraseña,nombre,curp,ciudad)
#                     ListaUsuarios.append(miUsuario)
#                     print("\nUsuario registrado\n")
#                     opcion = 0
#     elif opcion == 2:
#         usuario = input("\nIntroduzca su usuario: ")
#         contraseña = input("Introduzca su contraseña: ")
#         if ListaUsuarios == []:
#              print("\nNo hay usuarios registrados\n")
#              opcion = 0
#         else:
#             for obj in ListaUsuarios:
#                 if obj._usuario == usuario and obj._contraseña == contraseña:
#                       if obj._rol == "administrador":
#                            for objetos in ListaUsuarios:
#                                 print(objetos)
#                       else:
#                           print(obj+"\n")
#                           opcion = 0
#                           break
#                 else:
#                     print("\nEl usuario no existe\n")
#                     opcion = 0
#     elif opcion == 3:
#          break
#     else:
#         print("\nOpción no válida\n")
#         opcion = 0
# print("\nHasta luego!")