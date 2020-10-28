print('Saludo:\nHola como estas')

parrafo = input ('Ingrese un parrafo : ')

archivo = open ('parrafo.txt','w',encoding = 'UTF-8')
archivo.write(f'este es su parrafo: {parrafo}\n')
archivo.close()