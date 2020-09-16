#Ejercicios while
print("---Ejercicio1---")

preguntaNumero="Ingrese porfavor un numero entero o 0 para terminar : "
NumeroIngresado =int(input(preguntaNumero))
suma = 0

while(NumeroIngresado != 0) :
    suma += NumeroIngresado
    NumeroIngresado =int(input(preguntaNumero))

print(suma)

#Ejercicio while 2
print("---ejercicio2---")

preguntaNumero1 ="ingrese un numero entero porfavor : "
preguntaNumero2 ="ingrese un  numero mayor al primero  porfavor : "
numeroIngresado1 =int(input(preguntaNumero1))
numeroIngresado2 =int(input(preguntaNumero2))

while(numeroIngresado1>=numeroIngresado2) :
    numeroIngresado2=int(input(preguntaNumero2))

print(numeroIngresado1)
print(numeroIngresado2)

#Ejercicio while 3
print("---ejercicio3---")

preguntaNumeroA ="ingrese un numero entero porfavor : "
preguntaNumeroB ="ingrese un numero entero porfavor : "
numeroingresadoA =int(input(preguntaNumeroA))
numeroingresadoB =int(input(preguntaNumeroB))

while(numeroingresadoA<numeroingresadoB):
    numeroingresadoA =numeroingresadoB
    numeroingresadoB=int(input(preguntaNumeroB))

#Ejercicio while 4
print("---ejercicio4---")

total= 0
monto=float(input('Monto de una venta : '))
while (monto!=0):
    if (monto <0):
        print('Monto no valido')
    else:
        total=+monto
    monto=float(input('Monto de una venta :'))
if (total>1000):
    total -=total*0.1
print('Monto total a pagar : $',total)




























