import matplotlib.pyplot as plt

ciudades =['Medelli,','cali','Ibague','Cartagena']
personas =[23389,68565,45467,36736]
plt.bar(ciudades,personas)
plt.title('Ciudades vs. población')
plt.xlabel('Ciudades Colombianas')
plt.ylabel('Poblacion')
plt.savefig('GraficoCiudades.png')
plt.show()
