import numpy as np

def test1():
	#cria um array com 500 itens aleatorios de 0 a 1
	x = np.random.randn(1, 500)
	lenght = x.size
	print (lenght)

def criaNaOrdem(num):
	#cria um vetor numpy com valores de 0 a num-1
	return np.arange(num)

def createarray():
	a = np.array([
				 [[1,2],[2,3]],
                 [[2,3],[3,4]],
                 [[4,5],[5,6]],
                 [[6,7],[7,8]]
                ])
	print(type(a))
	print(a.ndim)

def multiplylists():
	a = np.array([2,3])
	b = np.array([3,2])
	print(a * b)

def returnSum(nparray):
	return nparray.sum()

def returnMax(nparray):
	return nparray.max()

def list_comprehension_with_nparray(nparray):
	return [x ** 3 for x in nparray if x % 2 == 0]

def randomInt():
	##Cria um nparray com 20 elementos inteiros aleatorios [0 1000)
	rand_arr = np.random.randint(0,1000,20)
	print(rand_arr)

print(list_comprehension_with_nparray(criaNaOrdem(10)))