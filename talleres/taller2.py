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

preguntaMonto="Por favor ingrese el monto de compra : "
preguntaMonto2="Por favor ingrese el siguiente monto o ponga 0 para finalizar : "
monto1 = float(input(preguntaMonto))
suma = 0
mensajeError ="ingrese por favor un monto positivo : "

while( monto1 <0):
    monto1=float(input(mensajeError))

while(monto1!= 0 ):
    suma += monto1
    monto2=float(input(preguntaMonto2))
    monto1 = monto2


if(suma>1000) :
    suma = suma-(suma*0.1)
    print(f"el valor que debes pagar con el descuento es {suma}")

print(suma)



























