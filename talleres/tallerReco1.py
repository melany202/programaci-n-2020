#ENTRADAS
listaDolares=[20000,30000,4000,2500,1000,7600]

#preguntas
preguntaMenu ='''
por favor ingrese una de estas opciones
            1-Convertir el dinero
            2-división de los ingresos mensuales
            3-ver ingreso mas alto, mas bajo y promedio
            4-para salir 
:'''
preguntaConversionDinero='''
            C-Mostrar el dinero en pesos Colombianos
            D-Mostrar el dinero en Dolares
            E-Mostrar el dinero en Euros
:'''

#MensajeError
mensajeEntradaNoValidaNumero='Recuerde ingresar una entrada valida 1,2,3,4'
mensajeEntradaNoValidaLetra='Recuerde ingresar una entrada valida C,D,E'
#MensajeInformativos
mensajeOpcion='Usted escogio la opcion {}'
mensajeSalida='Gracias por ingresar al programa'
mensajeDolares='No es necesaria la conversión pero se muestra la lista'
mensajeMaximo='Su ingreso mas alto fue'
mensajeMinimo='Su ingreso mas bajo fue'
mensajePromedio='El promedio de los ingresos fue'



#calculosPreliminares
listaColombianos=[]
listaEuros=[]
listaDolar=listaDolares
listaingresos=[]

#---Pasando de dolares a pesos---#
for elemento in listaDolar:
    Colombianos=elemento * 3700
    listaColombianos.append(Colombianos)

#---Pasando de dolares a euros---#
for elemento in listaDolar:
    euros= elemento * 0.84
    listaEuros.append(euros)

#---diviendo ingresos mensuales---#
for elemento in listaDolar:
    ingreso=''
    if(elemento < 1000):
        print('Ingresos bajos')
    elif(elemento >= 1000 and elemento < 7000):
        print('Ingresos medios')
    elif(elemento>= 7000 and elemento < 20000):
        print('Ingresos altos')
    else:
        print('Ingresos elevados')
    listaingresos.append(ingreso)

#---Calculae maximo,minimo y promedio---#
mayor=max(listaDolar)
menor=min(listaDolar)
suma= 0
for elemento in listaDolar:
    suma+= elemento
promedio=suma/len(listaDolar)

#MENU
#InicioCodigo
opcion=int(input(preguntaMenu))

while(opcion != 4):
    if(opcion ==1):
        print(mensajeOpcion.format(1))
        conversion=input(preguntaConversionDinero)
        if(conversion =='C'):
            print(listaColombianos)
        elif(conversion == 'D'):
            print(listaDolar)
        elif(conversion == 'E'):
            print(listaEuros)
        else:
            print(mensajeEntradaNoValidaLetra)
    elif(opcion==2):
        print(mensajeOpcion.format(2))
        print(listaingresos)
    elif(opcion ==3):
        print(mensajeOpcion.format(3))
        print(mensajeMaximo,mayor)
        print(mensajeMinimo,menor)
        print(mensajePromedio,promedio)
    else:
        print(mensajeEntradaNoValidaNumero)

    opcion=int(input(preguntaMenu))

print(mensajeSalida)
