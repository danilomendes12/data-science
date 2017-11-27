import matplotlib.pyplot as plt
import numpy as np

#run the program: python3 histogram.py

#cria a lista vazia
y = []

#preenche a lista vazia com 100000 numeros aleatorios
for x in range(0,1000000):
	y.append(np.random.randn())

#cria um histograma com a frequencia dividida em 500 intervalos
plt.hist(y, 500)
plt.title('Distribution of Random Numbers')
plt.show()
