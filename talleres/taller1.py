nombre =input("Buenas tardes por favor ingrese su nombre : ")
peso =int(input("Ingrese por favor su peso en kilogramos : "))
estatura =float(input("Ingrese por favor su estatura : "))

imc =peso/estatura**2
if (imc <18.5) :
    print(f"{nombre} tiene infrapeso")
elif (imc>=18.5 and imc<25) :
    print(f"{nombre} tiene peso normal")
elif (imc>=25 and imc<30) :
    print(f"{nombre} tiene sobrepeso")
elif (imc>=30 and imc<35) :
    print(f"{nombre} tiene obesidad")
else:
    print (f"{nombre} tiene obesidad morbida")
