import personas as p
import estudiante as es
import egresado as eg 
laura =p.Persona('Laura',18,1000567456)
mario =p.Persona('Mario',20,4567890765)
valeria = es.Estudiante('Valeria',18,345678678,'Biomedica',3)
laura.hablar('Todo anda muy bien, me gusta aprender ')
mario.comer('taco')
valeria.estudiar('calculo')
melany = eg.Egresado('Melany',18,12345675,'Biomedica','2023/12/12')
print(melany.semestre)
melany.trabajar('MIT')
