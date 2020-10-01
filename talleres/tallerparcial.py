
numero1= int(input('Ingrese por favor un numero : '))
numero2 = int(input('Ingrese por favor otro numero : '))

def infoNumero (numero1,numero2):
    if (numero1>numero2):
        print(f'el numero {numero1} es mayor al numero {numero2}')
    elif (numero2>numero1):
        print(f'el numero {numero2} es mayor que el numero {numero1}')
    else:
        print(f'los numeros son iguales')

infoNumero(numero1,numero2)

#dada una lista de nombres cree una funcion que muestre en pantalla nombre por nombre 

def nombres (lista):
    nombres=[]
    for elemento in (lista):
        print(elemento)

listaNombres=['mariana','sofia','camila','juan']
nombres(listaNombres)

#IMC
def IMC (peso, altura):
    return peso/(altura**2)
imc= IMC(60,1.64)
print(imc)

#recibe de entrada otra funcion y al final muestra la slaida de la funcion

def mostrarIMC (IMC,estatura,peso):
    imc=IMC (estatura,peso)
    print(f'El IMC calculado es de {imc}')

mostrarIMC(IMC,1.63,60)

#clases
class Persona:
    def __init__(self,idIngresado,nombreIngresado,pesoIngresado,alturaIngresado,sexoIngresado):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.altura = alturaIngresado
        self.sexo = sexoIngresado
    def atributos(self):
        print(f'soy una persona y  mi documento es  {self.id},mi nombre  es {self.nombre}, peso {self.peso}kg , mi altura es {self.altura},y soy de sexo  {self.sexo}')

#Creo el objeto 
melany = Persona('Melany',1000408785,59,1.64,'femenino')
#se muestran los atributos
melany.atributos()

class Estudiante (Persona):
    def __init__(self,idIngresado,nombreIngresado,pesoIngresado,alturaIngresado,sexoIngresado,carreraIngresada,semestreIngresada,uniIngresada):
        Persona.__init__(self,idIngresado,nombreIngresado,pesoIngresado,alturaIngresado,sexoIngresado)
        self.carrera = carreraIngresada
        self.semestre = semestreIngresada
        self.universidad = uniIngresada
        print ('se ha creado un nuevo estudiante')
    def atributos (self):
        print(f'soy una persona y  mi documento es  {self.id},mi nombre  es {self.nombre}, peso {self.peso}kg , mi altura es {self.altura},y soy de sexo  {self.sexo}')
    def clase (self, materia):
        print(f'hola soy {self.nombre} y voy a asistir a la clase de {materia}')

estudiante = Estudiante (1000408785,'Melany',59,1.64,'femenino','Ingeniria Biomedica',3,'CES')

estudiante.atributos()
estudiante.clase('programacion')







