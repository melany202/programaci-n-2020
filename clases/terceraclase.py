a = int (input("Ingrese el primer numero entero :  "))
b = int (input("Ingrese el segundo numero entero :  "))
print (a , b )

if (a == b):
    print("Son numeros iguales")
elif (a>b):
    print("el numero a" , a , "es mayor que el numero" ,b)
else:
    print(f"el numero b {b} es mayor que a {a}")

#Dada una temperatrura determinar si el paciente esta sano o no
# Temperatura menor a 36 grados hipotermia
# Temperatura en el intervalo  36-37.5 grados normal
#Temperatura en el intervalo 37.5-38 Alerta
# Temperatura mayor a 38 grados fiebre
#muestre el nombre del paciente y su estado

name = input("Ingrese el nombre del paciente : " )
temperatura = float (input("Ingrese la temperatura del paciente : "))
if (temperatura < 36) :
    print(f"El paciente llamado {name} se encuentra en estado de hipotermia")
elif (temperatura>=36 and temperatura <37.5) :
    print(f"El paciente llamado {name} se encuentra en estado favorable")
elif(temperatura>=37.5 and temperatura< 38) :
    print(f"El paciente llamado {name} se encunetra en estado de alerta")
else:
    print (f"El paciente llamado {name} se encuentra en estado de fiebre")
