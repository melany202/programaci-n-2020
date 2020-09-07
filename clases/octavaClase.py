import random

dado = random.randint(1,6)
print (dado)

numeroUsuario =int(input("Ingrese un numero"))
intentos = 0

while (numeroUsuario != dado):
    print ("No adivinaste el numero")
    intentos =intentos + 1
    numeroUsuario = int(input("Ingresa el otro numero : "))

print(f"Has realizado {intentos} intentos antes de adivinar el numero")
print("Felicitaciones")

