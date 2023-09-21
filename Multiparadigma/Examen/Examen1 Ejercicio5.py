def Ordenar(Lista):
    numeros = [x for x in Lista if x.isdigit()]
    letras = [x for x in Lista if not x.isdigit()]
    Lista = sorted(letras) + sorted(numeros)
    print(' '.join(str(x) for x in Lista))

ListaResultado = []
CadenaResultado = ""
opcion = 0
try:
    while opcion == 0:
        opcion = int(input("\nSeleccione una opción: \n1.-Añadir una cadena \n2.-Mostrar el resultado \n3.- Salida \nRespuesta: "))
        if opcion == 1:
            opcion = 0
            Cadena = input("\nIntroduzca un texto: \n")
            for n in Cadena:
                if n == " ":
                    ListaResultado.append(CadenaResultado)
                    CadenaResultado=""
                else:
                    CadenaResultado += n
            ListaResultado.append(CadenaResultado)
            CadenaResultado=""
        elif opcion == 2:
            opcion = 0
            Ordenar(ListaResultado)
        elif opcion == 3:
            break
        else:
             print("\nOpción no válida\n")
             opcion = 0
    print("\nHasta luego!")
except:
     print('Ocurrió un error')