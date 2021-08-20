#datos al azar
import random 
import matplotlib.pyplot as plt
print(random.randrange(10,100,2))

#acomodar lista
lista = [1,2,3,4,5,6,7,8,9,10]
print("Original",lista)

random.shuffle(lista)
print("mix",lista)
#generar grafica de gauss
campana = [random.gauss(1,0.5 ) for i in range (1000)]
print(campana)
plt.hist(campana,bins=15)
plt.show()