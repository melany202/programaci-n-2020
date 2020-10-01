#cree una funcion para cada uno de los puntos 
print('punto1')
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

print('punto2')
def numerosPares (lista):
    pares=[]
    for elemento in (lista):
        if (elemento % 2 ==0):
            pares.append (elemento)
    return pares 

listaNumeros=[34,87,98,65,13,14]
edadesPares= numerosPares(listaNumeros)
print(edadesPares)

print('punto3')
def mensaje ():
    print('hola soy una niña muy feliz, que tengas buen dia')
mensaje()

print('punto4')
def restar(valor) :
    return valor-12
resta = restar (50)
print(resta)

print('punto5')
def multiplicar(valor) :
    return valor*12
multiplicacion = multiplicar (2)
print(multiplicacion)

print('punto6')
def dividir(valor) :
    return valor/12
division = dividir(24)
print(division)

print('punto7')
def sumar(valor) :
    return valor+12
suma = sumar(100)
print(suma)

print('punto8')
def calculadora (accion,valor):
    print(accion(valor))
calculadora (sumar,1)
calculadora (dividir,24)
calculadora(multiplicar,2)
calculadora(restar, 38)

#ejercicios clases
class Paciente:
    def __init__(self,idIngresado,nombreIngresado,sexoIngresado,afiliadoIngresado):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.sexo = sexoIngresado
        self.afiliado = afiliadoIngresado
    def atributos (self):
        print(f'el paciente identificado con {self.id},su nombre es {self.nombre},de sexo {self.sexo} es afiliado a {self.afiliado}')
    def sintomas (self,lista):
        for elemento in (lista):
            print(elemento)

listaSintomas=['fiebre','tos','indigestion','dolor de garganta']

juan = Paciente(1000467897,'juan','masculino','sura')
juan.atributos()
juan.sintomas(listaSintomas)

class Estable (Paciente):
    def __init__(self, idIngresado,nombreIngresado,sexoIngresado,afiliadoIngresado,tiempoIngresado,temperaturaIngresada,animoIngresado):
        Paciente.__init__(self,idIngresado,nombreIngresado,sexoIngresado,afiliadoIngresado)
        self.tiempo = tiempoIngresado
        self.temperatura = temperaturaIngresada
        self.animo =animoIngresado
    def atributos (self):
        print(f'el paciente identificado con {self.id},su nombre es {self.nombre},de sexo {self.sexo} es afiliado a {self.afiliado},lleva en tiempo de espera {self.tiempo}minutos,tiene una temperatura de {self.temperatura} grados centigrados,y con un animo {self.animo}')
    def recomendaciones (self, lista):
        for elemento in (lista):
            print(f'el paciente debe {elemento}')

listaRecomendaciones=['descansar','dormir','ir a terapias']

andrea = Estable(1000567876,'andrea','femenino','sura',30,36,'bueno')
andrea.atributos()
andrea.recomendaciones(listaRecomendaciones)

class Critico (Paciente):
    def __init__(self, idIngresado,nombreIngresado,sexoIngresado,afiliadoIngresado,habitacionIngresado,patologiaIngresada):
        Paciente.__init__(self,idIngresado,nombreIngresado,sexoIngresado,afiliadoIngresado)
        self.habitacion = habitacionIngresado
        self.patologia = patologiaIngresada
    def atributos (self):
        print(f'el paciente identificado con {self.id},su nombre es {self.nombre},de sexo {self.sexo} es afiliado a {self.afiliado},se encunetra en la habitacion {self.habitacion} y su patologia es {self.patologia}')
    def sintomas (self,lista):
        for elemento in (lista):
            print(elemento)

listaSintomas =['inconciencia','fatiga','freceuncia cardiaca baja']

oscar = Critico(126757509,'oscar','masculino','sura',316,'aneurisma')
oscar.atributos()
oscar.sintomas(listaSintomas)






