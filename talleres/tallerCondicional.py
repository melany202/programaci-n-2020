#Ejercicio 1 condicionales
print('ejercicio 1')

preguntaNumero1='Ingrese un numero entero : '
preguntaNumero2='Ingrese otro numero entero : '

numero1=int(input(preguntaNumero1))
numero2=int(input(preguntaNumero2))

if(numero1>numero2):
    print(f'el {numero1} es mayor que el {numero2}')
elif(numero1==numero2):
    print('Los numeros son iguales')
else:
    print(f'el {numero2} es mayor que el {numero1}')

#Ejercicio 2 condicionales
print('ejercicio 2')

preguntaEdad='Ingrese por favor su edad : '

edad=int(input(preguntaEdad))

if(edad>=18 and edad<=25):
    print('Es usted una persona joven')
elif(edad>=26 and edad<=60):
    print('Es usted un adulto')
else:
    print('Es usted un adulto mayor')

#Ejercicio 3 condicionales
print('ejercicio 3')

preguntAñoActual='por favor ingrese el año actual : '
preguntaAñoCualquiera='por favor ingrese un año cualquiera: '

añoActual=int(input(preguntAñoActual))
añoCualquiera=int(input(preguntaAñoCualquiera))

mensaje='{}{} años'

if(añoCualquiera>añoActual):
    resta=añoCualquiera - añoActual
    print(mensaje.format('han pasado', resta))
elif(añoActual>añoCualquiera):
    resta=añoActual - añoCualquiera
    print(mensaje.format('faltan',resta))
else:
    print('los años son iguales')

#Ejercicio 4 condicionales
print('ejercicio 4')

#---preguntas---#
preguntaMedida='Ingrese por favor una distancia en centimetros : '
preguntaUnidades='''ingrese en que unidades desea transformar:
            K-Kilometros
            M-Metros
            mm-Milimetros 
'''

mensajeError='Entrada no valida,repita por favor'

#---entradas---#
medida=float(input(preguntaMedida))
Unidades=input(preguntaUnidades)

#---conversiones---#
Metros= medida/100
kilometos=medida*10**5
Milimetros=medida*10

if(Unidades=='K'):
    print(kilometos)
elif(Unidades=='M'):
    print(Metros)
elif(Unidades=='mm'):
    print(Milimetros)
else:
    print(mensajeError)


