procedencia =input("Buenas tardes por favor ingrese su procedencia : ")
if (procedencia == "china" or procedencia=="iran" or procedencia=="italia") :
    print(f"señor procedente de {procedencia} usted se debe quedar en estado de observación")
else:
    temperatura =float(input("ingrese por favor su temperatura : "))
    if (temperatura < 36) :
        print(f"señor procedente de {procedencia} usted esta en estado de hipotermia")
    elif (temperatura>=36 and temperatura<38.5) :
        print(f"señor procedente de {procedencia} usted esta en estado saludable")
    elif (temperatura >=38.5 and temperatura<=40) :
        print(f"señor procedente de {procedencia} usted esta en estado de alerta")
    else:
        print (f"señor procedente de {procedencia} usted esta en estado peligroso")

