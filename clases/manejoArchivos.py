#leer

archivo = open ('poema.txt', encoding = 'UTF-8')
print(archivo)
lineas = archivo.readlines()
archivo.close()
print(lineas)
listaReglones =[]
with open ('poema.txt', encoding = 'UTF-8') as lineas:
    for line in lineas:
        print(line)
        listaReglones.append(line)

print(listaReglones)

print('Saludo:\nHola como estas')


nombre = input ('Ingrese su nombre : ')
edad = int(input('Ingrese su edad : '))
opinion = input('Ingrese su opinion : \n')

archivo = open ('opinion.txt','w',encoding = 'UTF-8')
archivo.write(f'opinion de {nombre}\n')
archivo.write(f'edad de {nombre}\n')
archivo.write(f'reseña:\n {opinion}')
archivo.close()

