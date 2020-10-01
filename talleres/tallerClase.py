#ejercicio 1 
print('Ejercicio 1')
class Torta:
    def __init__(self,formaIngresada,saborIngresado,alturaingresada):
        self.forma = formaIngresada
        self.sabor = saborIngresado
        self.altura = alturaingresada
    def atributos (self):
        print(f'la torta es de forma {self.forma},es de {self.sabor},y tiene una altura de {self.altura} cm')

torta1 = Torta('redonda','chocolate',50)

torta1.atributos()

#ejercicio 2
print('Ejercicio 2')
class Estudiante:
    def __init__(self,edadIngresada,nombreIngresada,idIngresada,carreraIngresada,semestreingresada):
        self.edad = edadIngresada
        self.nombre = nombreIngresada
        self.id = idIngresada
        self.carrera = carreraIngresada
        self.semestre = semestreingresada
        print ('se ha creado un estudiante')
    def atributos (self):
        print(f'soy un estudiante y  tengo   {self.edad} años,mi nombre  es {self.nombre}, mi documento es {self.id} , estudio {self.carrera},y voy en el  {self.semestre} semestre ')
    def clase (self, materia,tiempo):
        print(f'hola soy {self.nombre} y voy a asistir a la clase de {materia} {tiempo} horas')
    
estudiante1 = Estudiante(20,'Melany',1000408785,'Biologia',6)
estudiante1.atributos()
estudiante1.clase('ciencia',3)

#ejercicio 3
print('Ejercicio 3')
class Nutricionista:
    def __init__(self,edadIngresada,nombreIngresado,universidadIngresada):
        self.edad = edadIngresada
        self.nombre = nombreIngresado
        self.universidad = universidadIngresada
    def atributos (self):
        print(f'Hola soy un nutricionista tengo {self.edad} años,me llamo {self.nombre},y soy egresado de la universidad {self.universidad}')
    def calcular_imc (self,peso, altura):
        return peso/(altura**2)
        

nutricionista1 = Nutricionista(30,'Javier','CES')
nutricionista1.atributos()
imc = nutricionista1.calcular_imc(48,1.50)
print(f'el imc calculado es {imc}')



#ejercicio4
print('Ejercicio 4')
class Canguro:
    def __init__(self,edadIngresada,idIngresada,nombreingresado):
        self.edad = edadIngresada
        self.id = idIngresada
        self.nombre = nombreingresado
    def atributos (self):
        print(f'hola soy un canguro tengo {self.edad}años, mi identificacion es {self.id},y me llamo {self.nombre}')
    def saltar (self,saltos):
        for elemento in range(saltos):
            print(f'el canguro a dado {elemento +1} saltos')

canguro1 =Canguro(10,1000409897,'Roberto')
canguro1.atributos()
canguro1.saltar(5)

#ejercicio5
print('Ejercicio 5')
class Flauta:
    def __init__(self,marcaIngresada,tipoIngresada):
        self.marca =marcaIngresada
        self.tipo =tipoIngresada
    def atributos (self):
        print(f'la flauta de de marca {self.marca} y es de tipo {self.tipo}')
    def cancion (self,cancion):
        print(f'la cancion {cancion} se interpreta con flauta')

flauta1 = Flauta('yamaha','dulce')
flauta1.atributos()
flauta1.cancion('mañanitas')









