#---se crea la listaNombre--#
listaNombre = []
listaNombre = ["Melany",
        "Karla",
        "Laura Paredes",
        "Laura montoya",
        "Juan pablo",
        "Mario",
        "Valeria",
        "Santiago"]

listaedades=[20,18,18,18,21,20,18,18]
print(listaNombre)
print(listaNombre[2])
print(listaNombre[-1])
listaNombre.append("Daniel")
print(listaNombre[-1])
print(listaNombre)

listaNombre.pop(-1)
print(listaNombre)
listaNombre.append("Daniel")
listaedades.append(27)
sizeList =len (listaNombre)
print (sizeList)

for i in range (sizeList):
    print(f"hola soy {listaNombre [i]} y estoy feliz programando")
print("segundo metodo")
for nombre in listaNombre:
    print (nombre)
    print(f"hola soy {nombre} y estoy fliz programando")

for i in range (sizeList):
    print (f"Nombre : {listaNombre[i]} Edad: {listaedades [i]}")

listaHobbies =[]
decision =0
while(decision==0):
    hobbie = input("Cual es tu hobbie favorito? :")
    listaHobbies.append(hobbie)
    decision =int (input("""Ingrese :
            0-para seguir agregando Hobbies
            !0-Para finalizar
    : """))
print (listaHobbies)
