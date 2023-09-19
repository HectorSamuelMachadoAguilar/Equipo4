import random

n = int(input("Ingrese el valor de N: "))

if n >= 2 and n <= 10:
    matrizA = []

    for fila in range(0,n):
        
        fila = []
        for columna in range(0,n):
            fila.append(random.randint(0,99))
            
        matrizA.append(fila)

    print(matrizA)
    matrizOrdenar = []
    
    for i in matrizA:
        for j in i:
            matrizOrdenar.append(j)
        
    matrizOrdenar.sort()
    print(matrizOrdenar)
    
    MatrizB = []
    for fila in range(0,n):
        
        fila = []
        for columna in range(0,n):
            fila.append(0)
        MatrizB.append(fila)





    vueltas = 0
    Contador = 0
            
    #while Con
    
    #fila 0
    lista1 = []
    for columna1 in range(0,n):
        MatrizB[0+vueltas][columna1] = matrizOrdenar[Contador]
        Contador += 1
    
    
    lista1 = []
    for fila1 in range(1,n):
        MatrizB[fila1][n-1] = matrizOrdenar[Contador]
        Contador += 1
        
    for columna2 in range(n-2,-1,-1):
        print (columna2)
        MatrizB[n-1][columna2] = matrizOrdenar[Contador]
        Contador += 1
        
    if Contador <= n:
        for fila2 in range(n-2,1,-1):
            MatrizB[fila2][0+vueltas] = matrizOrdenar[Contador]
            Contador += 1
        
        vueltas += 1
        
    else:
        #break
        print(MatrizB)
        
    
else:
    print("El valor de N debe ser entre mayor que 1 y menor que 11")