#ejercicio 1

print('ejercicio 1')

def mostrarLista (lista):
    for elemento in (lista):
        print(elemento)

comida=['pasta','arroz','carne','pollo']
mostrarLista(comida)

#ejercicio 2

print('ejercicio 2')

def listaNum (lista):
    mayor = max(lista)
    menor = min(lista)
    suma=0
    for elemento in (lista):
        suma += elemento 
        promedio=suma/len(lista)
    print(f'el numero mayor en la lista es el {mayor},el numero menor es el {menor} y el promedio es {promedio}')

numeros=[23,56,76,45,67]
listaNum(numeros)

#ejercicio 3

print('ejercicio 3')

def saludo(cantidad =0 ) :
    print('Hola como estas '*cantidad)
saludo(12)

#ejercicio 4

print('ejercicio 4')

def numerosPares (lista):
    pares=[]
    for elemento in (lista):
        if (elemento % 2 ==0):
            pares.append (elemento)
    return pares 

listaNumeros=[34,87,98,65,13,14]
edadesPares= numerosPares(listaNumeros)
print(edadesPares)


#ejercicio 5

print('ejercicio 5')

def numerosMayores (lista):
    mayores=[]
    for elemento in (lista):
        if (elemento> 24):
            mayores.append (elemento)
    return mayores

edades=[34,67,12,19,9,74,32]
edadesMayores=numerosMayores(edades)
print(edadesMayores)

#ejericio 6

print('ejercicio 6')

def IMC (peso, altura):
    return peso/(altura**2)
imc= IMC(60,1.64)
print(imc)

#ejercicio 7

print('ejercicio 7')

def chao ():
    print('hasta luego, grcaias por usar el codigo')
chao()


