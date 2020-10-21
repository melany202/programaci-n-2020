import funcionesarchivos as helper
helper.agregarLinea ('opinion.txt','Nueva linea')
renglonesLibro = helper.leerArchivos('libro.txt')
print(len(renglonesLibro))

if (len(renglonesLibro)==0):
    print('es la primera linea que se escribira en el libro')
    helper.agregarLinea('libro.txt','el dia que prograr fue facil')
else:
    linea = input('Ingrese la linea que desea agregar : \n')
    helper.agregarLinea ('libro.txt',linea)
