class Persona:
    def __init__(self,estaturaIngresado,pesoIngresado,nombreIngresado,idIngresado,edadingresado):
        self.raza='Humana'
        self.estatura = estaturaIngresado
        self.edad = edadingresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.id = idIngresado
        print('Hola mundo estoy viv@')
    def caminar (self):
        print('Hola voy a caminar')
    def saludo (self,saludoespecial):
        print(saludoespecial)
class Arquitecto (Persona):
    def dibujarPlanos (self):
        print(f'Hola soy {self.nombre} voy a dibujar el plano')
class Biomedico(Persona):
    def cultivarcelulas (self):
        print(f'Hola soy {self.nombre} voy a cultivar celulas')

karla = Arquitecto(1.62,48,'karla',1000345675,18)
karla.caminar()
juan = Biomedico(1.76,82,'Juan Pablo',1200467890,23)
juan.caminar()
karla.saludo('HOLI CRAYOLI')
juan.saludo('HOLA COCACOLA')
karla.dibujarPlanos()
juan.cultivarcelulas()



