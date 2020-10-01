#ejercicio 1
print('Ejercicio1')
class Persona:
    def __init__(self,idIngresado,nombreIngresado,edadIngresada):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.edad = edadIngresada
    def hablar (self,mensaje):
        print(f'la persona llamada {self.nombre} escribio: {mensaje}')
    def caminar (self,pasos):
        print(f'la persona llamada {self.nombre} ha caminado {pasos} pasos')

juliana = Persona(1000409789,'Juliana',20)
juliana.hablar('hola estoy feliz')
juliana.caminar(30)

#ejercicio 2
print('Ejercicio2')
class Doctor (Persona):
    def __init__(self, idIngresado,nombreIngresado,edadIngresada,especialidadIngresada):
        Persona.__init__(self,idIngresado,nombreIngresado,edadIngresada)
        self.especialidad = especialidadIngresada
    def atributos (self):
        print(f'hola soy doctor y mi id es {self.id},me llamo {self.nombre},tengo {self.edad} años y mi especialidad es {self.especialidad}')
    def tratar (self,enfermedad):
        print(f'procedo a tratar {enfermedad}')

camilo = Doctor(1000408786,'camilo',20,'dermatologo')
camilo.atributos()
camilo.tratar('dermatitis')

#ejercicio 3
print('Ejercicio3')
class Nutricionista (Persona):
    def __init__(self, idIngresado,nombreIngresado,edadIngresada,universidadIngresada):
        Persona.__init__(self,idIngresado,nombreIngresado,edadIngresada)
        self.universidad = universidadIngresada
    def atributos (self):
        print(f'hola soy nutricionista mi id es {self.id},me llamo {self.nombre},tengo {self.edad} años y soy egresada del {self.universidad}')
    def calcular_imc (self, peso, altura):
        return peso/(altura**2)

simon = Nutricionista(1000567896,'simon',21,'CES')
simon.atributos()
imc = simon.calcular_imc(80,1.67)
print(f'el imc calculado es {imc}')

#ejercicio 4
print('Ejercicio 4')
class Abogado (Persona):
    def __init__(self,idIngresado,nombreIngresado,edadIngresada,especialidadIngresada,universidadIngresada):
        Persona.__init__(self,idIngresado,nombreIngresado,edadIngresada)
        self.especialidad = especialidadIngresada
        self.universidad = universidadIngresada
    def atributos (self):
        print(f'hola soy abogado mi id es {self.id},me llamo {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad} y soy egresad@ de {self.universidad}')
    def caso (self, nombre, caso):
        print(f'procedo a representar al cliente {nombre} en el caso {caso}')

daniel = Abogado(1000498786,'daniel',28,'penal','CES')
daniel.atributos()
daniel.caso('jualian','asesinato')

