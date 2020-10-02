#primera parte 
print('punto1')
def elevar2(valor) :
    return valor**2
numeroElevado = elevar2 (4)
print(numeroElevado)

print('punto2')
def elevar3(valor):
    return valor**3
numeroelevado =elevar2 (3)
print(numeroelevado)

print('punto3')
def elevar4(valor):
    return valor**4
numeroelevado1 =elevar4 (2)
print(numeroelevado1)

print('punto4')
def elevar5 (valor):
    return valor**5
numeroelevado2 =elevar5(3)
print(numeroelevado2)

print('punto5')
def calculadora (accion,valor):
    print(accion(valor))
calculadora (elevar2,5)
calculadora (elevar3,3)
calculadora(elevar4,2)
calculadora(elevar5,6)

#segundaParte
class Doctor:
    def __init__(self,idIngresado,nombreIngresado,sexoIngresado,universidadIngresado):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.sexo = sexoIngresado
        self.universidad = universidadIngresado
    def atributos (self):
        print(f'Hola soy un doctor mi id es {self.id},me llamo {self.nombre} soy de sexo {self.sexo} y soy egresado del {self.universidad}')
    def sintomas (self,lista):
        for elemento in (lista):
            print(elemento)

listaSintomas =['fiebre','nauseas','tos','dolor de estomago']
juan = Doctor(1000456786,'juan','masculino','CES')
juan.atributos()
juan.sintomas(listaSintomas)

class Neurologo (Doctor):
    def __init__(self,idIngresado,nombreIngresado,sexoIngresado,universidadIngresado,experienciaIngresada,consultorioIngresado,salarioIngresado):
        Doctor.__init__(self,idIngresado,nombreIngresado,sexoIngresado,universidadIngresado)
        self.experiencia = experienciaIngresada
        self.consultorio = consultorioIngresado
        self.salario = salarioIngresado
    def atributos (self):
        print(f'Hola soy un@ doctor mi id es {self.id},me llamo {self.nombre} soy de sexo {self.sexo} y soy egresado del {self.universidad},tengo {self.experiencia} de experiencia, trabajo en el consultorio {self.consultorio},y mi salario es de {self.salario} de pesos')
    def pacientes (self,lista):
        for elemento in (lista):
            print(f'Atenderé al paciente {elemento}')

listaPacientes =['Emilio','Juanita','Sofia','Simón']
carlos = Neurologo(1000467876,'Carlos','masculino','CES',10,3,'Diez millones')
carlos.atributos()
carlos.pacientes (listaPacientes)

class Cardiologo (Doctor):
    def __init__(self,idIngresado,nombreIngresado,sexoIngresado,universidadIngresado,experienciaIngresada,consultorioIngresado,salarioIngresado):
        Doctor.__init__(self,idIngresado,nombreIngresado,sexoIngresado,universidadIngresado)
        self.experiencia = experienciaIngresada
        self.consultorio = consultorioIngresado
        self.salario = salarioIngresado
    def atributos (self):
        print(f'Hola soy un@ doctor mi id es {self.id},me llamo {self.nombre} soy de sexo {self.sexo} y soy egresado de la universidad {self.universidad},tengo {self.experiencia} años de experiencia, trabajo en el consultorio {self.consultorio},y mi salario es de {self.salario} de pesos')
    def sintomas (self,lista):
        for elemento in (lista):
            print(elemento)


listaSintomas =['mareo','aturdimiento','apneas','dolor en el pecho']
elizabeth = Cardiologo (987876786,'Elizabeth','femenino','UdeA',15,10,'veinte millones')
elizabeth.atributos()
elizabeth.sintomas(listaSintomas)

print('YA SE QUE TIENE ESTE PACIENTE')

