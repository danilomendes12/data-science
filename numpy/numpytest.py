import numpy as np

def test1():
	x = np.random.randn(1, 500)
	lenght = x.size
	print (lenght)

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

test1()
createarray()
multiplylists()