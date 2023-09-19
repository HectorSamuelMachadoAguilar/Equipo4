Lista = []
try:
    n1 = int(input('Dime el primer número: '))
    n2 = int(input('Dime el segundo número: '))

    if n1 < 100 or n1 > 999:
        print('El primer valor no es de 3 digitos')
    elif n2 < 100 or n2 > 999:
        print('El segundo valor no es de 3 digitos')
    else:
        n1 = int(str(n1)[::-1])
        n2 = int(str(n2)[::-1])

        if n1 > n2:
            print(f"El primer número es mayor: {n1}")
        else:
            print(f'El segundo número es mayor: {n2}')
except:
    print('Ocurrió un error')