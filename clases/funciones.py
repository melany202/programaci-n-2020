#funciones sin entrada
def lineDesign():
    print('#'*60)
lineDesign()

def lineDesign() :
    print('hola')
    print('como estas')
lineDesign()

#funciones con una entrada
def lineDesignC(cantidad) :
    print('#'*cantidad)
lineDesignC(12)

#funcion suma

def sumar(valor1=0,valor2=0):
    return valor1 + valor2
print(sumar(2,2))
def restar(valor1=0,valor2=0):
    return valor1 - valor2
print(sumar(2,2))
def multiplicar(valor1=0,valor2=1):
    return valor1 * valor2
print(sumar(2,2))
def dividir(valor1=0,valor2=1):
    return valor1 / valor2
print(sumar(2,2))

#funciones que utilizan otras 
def calculadora (accion,valor1,valor2):
    print(accion(valor1,valor2))
lineDesignC(30)
calculadora (sumar, 1,1)
calculadora (dividir, 1,2)
calculadora(multiplicar,73,77)
calculadora(restar, 73,77)