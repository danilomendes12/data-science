import matplotlib.pyplot as plt
import numpy as np

N=1000
x = np.random.randn(N)
y = np.random.randn(N)

area= (5 * np.random.rand(N))**3 
colors = ['magenta', 'blue', 'black', 'yellow']

fig = plt.figure()
#posicao do subplot na imagem
imgage2 = fig.add_subplot(111)
plt.scatter(x, y, s=area, c=colors, alpha=0.6)
#ativa o grid
imgage2.grid(True)
plt.show()


def saveFigure():
	# Save Figure
	plt.savefig("images/pop.png")

	# Save Transparent Figure
	plt.savefig("images/pop2.png", transparent=True)