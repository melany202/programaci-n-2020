#ENTRADAS
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#Preguntas
preguntaMenu = '''
Por favor igrese alguna de estas opciones 
            1-Convertir temperaturas
            2-Estado de salud de c/u de las temperaturas
            3-Ver maximo y minimo de temperaturas
            4-Para salir del programa
: '''
preguntaConversionTemperatura = '''
            F-Convertir temperaturas Fahrenheit
            K-Covertir temperaturas kelvin 
            C-Convertir temperaturas Celsius
: '''


#---Mensaje Error---#
mensajeEntradaNoValidaN ='Recuerde ingresar una opcion valida 1,2,3,4'
mensajeEntradaNoValidaT ='Recuerde ingresar una opcion valida F,K,C'
#---Mensajes Informativos---#
mensajeOpcion = 'Usted escogio la opcion {}'
mensajeSalida ='Gracias por usar el programa'
mensajeCelsius ='No es necesario la conversión, pero se muestra la lista'
mensajeMaxima ='La temperatura maxima es'
mensajeMinima ='La temperatura minima fue'
mensajefrecuencia ='La temperatura fue tomada con una frecuencia de'



#Inicio codigo
opcion =int(input(preguntaMenu))
#Calculos preliminares
listaGradosKelvin =[]
listaGradosFa=[]
listaGradosC =Temperatura_Corporal
ListaEstadosSalud =[]

#---Pasando a kelvin xC + 273.15---#
for elemento in listaGradosC:
    kelvin = elemento + 273.15
    listaGradosKelvin.append(kelvin)

#---Pasando a Fa=(xC*1.8)+32 ---#
for elemento in listaGradosC:
    Fahrenheit = (elemento*1.8)+32
    listaGradosFa.append(Fahrenheit)

#---detectando los estados de salud---#
for elemento in listaGradosC:
    estado =''
    if (elemento < 36):
        estado= 'Hipotermia'
    elif(elemento >= 36 and elemento <37.6 ):
        estado ='Normal'
    else:
        estado ='Fiebre'
    ListaEstadosSalud.append(estado)

#---Calcular maximo & minimo---#
mayor = max (listaGradosC)
menor =min (listaGradosC)
frecuencia =len(listaGradosC)/24








#Menu
while (opcion != 4) :
    if (opcion == 1):
        print(mensajeOpcion.format(1))
        #pregunta conversion
        conversion =input(preguntaConversionTemperatura)
        if(conversion =='K'):
            print(listaGradosKelvin)
        elif (conversion =='F'):
            print(listaGradosFa)
        elif(conversion =='C'):
            print(listaGradosC)
        else :
            print(mensajeEntradaNoValidaT)


    elif(opcion ==2):
        print(mensajeOpcion.format(2))
        print(ListaEstadosSalud)
    elif(opcion ==3):
        print(mensajeOpcion.format(3))
        print(mensajeMaxima,mayor)
        print(mensajeMinima,menor)
        print(mensajefrecuencia,frecuencia)
    else:
        print(mensajeEntradaNoValidaN)

#Entrada de la variable de opcion 
    opcion =int(input(preguntaMenu))


#Salida del programa
print(mensajeSalida)





