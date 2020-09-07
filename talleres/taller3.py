#ejercicio 1
print("---ejercicio1 for---")

suma = 0
for i in range(101):
    suma += i
print(suma)

#ejercicio 2
print("---ejercicio2 for---")

preguntaNumero ="Ingrese un numero entero : "
numero1= int(input(preguntaNumero))
factorial = 1

for i in range(numero1):
    factorial=factorial * (i+1)
print(factorial)

#ejercicio 3
print("---ejercicio3 for---")

sumaPositivo=0
cantidadPositivos=0
sumaNegativos=0
preguntaNumero="ingrese un numero entero"
for i in range(6):
    numero=int(input(preguntaNumero))
    if (numero>0):
        sumaPositivo=sumaPositivo+numero
        cantidadPositivos=cantidadPositivos+1
    else:
        sumaNegativos=sumaNegativos+numero
print("suma de los negativos:",sumaNegativos)
if (cantidadPositivos!=0):
    print("promedio de los positivos :",sumaPositivo/cantidadPositivos)
else:
    print("No se ingresaron numeros negativos")

#ejercicio 4
print("---ejercicio4 for---")
listaCanciones=["relacion","hawai","caramelo","linda","mojaita"]

sizeList =len (listaCanciones)
for i in range(sizeList):
    print(listaCanciones[i])

import random
cancionAleatoria = random.randint(0,4)
print(f"se escogio esta cancion: {listaCanciones[cancionAleatoria]}")










