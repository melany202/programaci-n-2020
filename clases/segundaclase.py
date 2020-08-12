nombre =input("Ingrese el nombre : ")
print ("Hola" , nombre, "eres bienvenido a este código")
edad = int(input("Por favor ingrese su edad : "))
estatura = float(input("Por favor ingrese su estatura : "))

print (edad)
print (estatura)

print (type(nombre))
print (type(edad))
print (type(estatura))      

if (edad >= 18):
    print ("Usted es mayor de edad")

if (estatura>1.70):
    print("Hola eres muy alto")

print ("Chao!! que te vaya super bien")