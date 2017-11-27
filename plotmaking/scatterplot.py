import math
import matplotlib.pyplot as plt
import numpy as np

#cria um diagrama de dispersão
#run the program: python3 scatterplot.py

def plot1():
	radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
	area = [round((r**2)*math.pi,2) for r in radius]
	print(area)


	plt.rcParams["figure.figsize"] = (15,7)
	plt.xlabel('Radius')
	plt.ylabel('Area')
	plt.title('Radius of Circle v Area')
	#s = the size of the dot
	plt.scatter(radius, area, color='g', s=30)

	plt.show()

def plot2():
	plt.rcParams["figure.figsize"] = (15,7)

	x = np.random.randn(1, 500)
	y = np.random.randn(1,500)
	plt.scatter(x, y, color='b', s=50)
	plt.xlabel('X axis')
	plt.ylabel('Y axis')
	plt.title('Scatter Plot')
	plt.show()

plot1()
plot2()


