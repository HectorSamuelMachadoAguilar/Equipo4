x = 1 #Enteros
y = 2.2 #Flotantes
#z = 2+3j #Complejos

print(type(x),type(y)#,type(z)
      )
print(id(x),id(y)#,id(z)
      )
xflotante = float(x)
ycomplejo = complex(y)
#zentero = int(z)
print(x,y#,z
      )
print(type(xflotante),type(ycomplejo)#,type(zentero)
      )
print(xflotante,ycomplejo)

#Boleanos
x=True # 1 = true
if x :
    print('x')

y=False # 0 = false
if not y :
    print('y')

x=[]
if bool(x):
    print('x list')

x={}
if bool(x):
    print('x dict')

x={0}
if bool(x):
    print('x set')

#Cadena
x = "Hola mundo"
y=5
print(x)
saludo = f'Saludo: {x}, Despedida: {y}'
print(saludo)
saludo = 'Saludo: '+x +', Despedida: '+str(y)
print(saludo)
texto=f"""
Hola
{saludo}
Adios
{y}
"""
print(texto)

x=5
y=6
z=7
print(x,y,z,sep='---',end='|')

nombre="Hector Machado"
print(nombre[::-1])