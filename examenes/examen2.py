listaPesos=[20000,30000,4000,2500,1000,7600]

#preguntas
preguntaMenu ='''
por favor ingrese una de estas opciones
            1-Convertir el dinero
            2-Agregar un nuevo valor a la lista
            3-Mostrar el ingreso mas alto,mas bajo y promedio 
            4-Eliminar un elemento de la lista
            5-Salir del programa  
:'''
preguntaConversionDinero='''
            C-Mostrar el dinero en pesos Colombianos
            D-Mostrar el dinero en Dolares
            E-Mostrar el dinero en Euros
:'''

#MensajeError
mensajeEntradaNoValidaNumero='Recuerde ingresar una entrada valida 1,2,3,4,5'
mensajeEntradaNoValidaLetra='Recuerde ingresar una entrada valida C,D,E'
#MensajeInformativos
mensajeOpcion='Usted escogio la opcion {}'
mensajeSalida='Gracias por ingresar al programa'
mensajePeso='No es necesaria la conversión pero se muestra la lista'
mensajeAgregar='Agregue a la lista el valor que desee : '
mensajeQuitar='retire el elemento que desee,ingresando 0 como primera posicion  : '
mensajeMaximo='Su ingreso mas alto fue'
mensajeMinimo='Su ingreso mas bajo fue'
mensajePromedio='El promedio de los ingresos fue'


#calculosPreliminares
listaColombiano=listaPesos
listaEuros=[]
listaDolares=[]
listaingresos=[]


#---Pasando de pesos a dolares---#
for elemento in listaColombiano:
    dolar=elemento * 0.00027
    listaDolares.append(dolar)

#---Pasando de pesos a euros---#
for elemento in listaColombiano:
    euros= elemento * 0.00023
    listaEuros.append(euros)


#---Calculae maximo,minimo y promedio---#
mayor=max(listaColombiano)
menor=min(listaColombiano)
suma= 0
for elemento in listaColombiano:
    suma+= elemento
promedio=suma/len(listaColombiano)



#InicioCodigo
opcion=int(input(preguntaMenu))

while(opcion != 5):
    if(opcion ==1):
        print(mensajeOpcion.format(1))
        conversion=input(preguntaConversionDinero)
        if(conversion =='C'):
            print(listaColombiano)
            print(mensajePeso)
        elif(conversion == 'D'):
            print(listaDolares)
        elif(conversion == 'E'):
            print(listaEuros)
        else:
            print(mensajeEntradaNoValidaLetra)
    elif(opcion==2):
        print(mensajeOpcion.format(2))
        agregar = float(input(mensajeAgregar))
        listaColombiano.append(agregar)
        print(listaColombiano)
    elif(opcion==3):
        print(mensajeOpcion.format(3))
        print(mensajeMaximo,mayor)
        print(mensajeMinimo,menor)
        print(mensajePromedio,promedio)
    elif(opcion==4):
        print(mensajeOpcion.format(4))
        print(listaColombiano)
        quitar=int(input(mensajeQuitar))
        listaColombiano.pop(quitar)
        print(listaColombiano)

    else:
        print(mensajeEntradaNoValidaNumero)

    opcion=int(input(preguntaMenu))

print(mensajeSalida)








