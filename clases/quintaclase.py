#------Preguntas-----#
preguntaNumero = "Ingrese un numero del 1 al 10 : "
#----Mensaje----#
mensajeFallido = "Fallaste!!, no es el numero secreto"
mensajeExitoso ="Felicitaciones has acertado el numero en el que pensé"
mensajeDespedida ="Gracias por jugar nos vemos"
mensajeDerrota ="Lo siento has perdido"
mensajeVida = "ten cuidado has perdido {} vida te quedan {}"

#Ciclos while

numeroSecreto =6
numeroIngresado = int(input(preguntaNumero))
vidasPerdidas=0
while(numeroSecreto!= numeroIngresado and vidasPerdidas<=2):
    vidasPerdidas =vidasPerdidas +1
    print(mensajeVida.format(vidasPerdidas,3-vidasPerdidas))
    print(mensajeFallido)
    if vidasPerdidas<3:
        numeroIngresado =int(input(preguntaNumero))

if vidasPerdidas <3:
    print(mensajeExitoso)
else:
    print(mensajeDerrota)
    print(mensajeDespedida)


preguntaVocal ="Ingrese una vocal en minuscula : "
mensajeFallido = "Fallaste!! , no es la vocal secreta"
mensajeExitoso ="Felicitaciones has acertado la vocal secreta"

vocalSecreta ="a"
vocalIngresada = input(preguntaVocal)
while(vocalSecreta!= vocalIngresada):
    print(mensajeFallido)
    vocalIngresada = input(preguntaVocal)
print (mensajeExitoso)
print(mensajeDespedida)