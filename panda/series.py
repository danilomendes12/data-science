import pandas as pd
import numpy as np
import matplotlib

def firstSimpleSerie():
	simpleSerie = pd.Series(np.random.randint(0,10,5))
	return simpleSerie

def firstSimpleSerieWithIndex():
	simpleSerie = pd.Series(np.random.randint(0,10,5), index = ['a','b','c','d','e'])
	return simpleSerie

def simpleSerieFromDictionary():
	dict_01 = {'Gavin' : 50, 'Russ' : 100, 'Erlich' : 150}
	simpleSerie = pd.Series(dict_01)
	return simpleSerie

def indexTest():
	simpleSerie = pd.Series(np.random.randint(0,10,5), index = ['a','b','c','d','e'])
	return simpleSerie['a'] # == simpleSerie[0]

def getAllMaiorQueNumero(numero):
	simpleSerie = pd.Series(np.random.randint(0,10,5), index = ['a','b','c','d','e'])
	return simpleSerie[simpleSerie>numero]

def getPares():
	simpleSerie = pd.Series(np.random.randint(0,10,5), index = ['a','b','c','d','e'])
	return simpleSerie[simpleSerie%2==0]

def getIndex():
	simpleSerie = pd.Series(np.random.randint(0,10,5), index = ['a','b','c','d','e'])
	return simpleSerie[['a','b','c']]

def multiplySeries():
	#multiplica os numeros com indices iguais(a = a, b = b, etc..)
	simpleSerie1 = pd.Series([1,2,3,4,5], index = ['d','a','e','b','c'])
	simpleSerie2 = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
	return simpleSerie1 * simpleSerie2

def sumSeries():
	#soma os numeros com indices iguais
	simpleSerie1 = pd.Series([1,2,3,4,5], index = ['d','a','e','b','c'])
	simpleSerie2 = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
	return simpleSerie1 + simpleSerie2

def serieWithNan():
	dict_01 = {'Gavin' : 50, 'Russ' : 100, 'Erlich' : 150}
	index = ['Gavin', 'Russ', 'Erlich', 'Peter']
	simpleSerie = pd.Series(dict_01, index=index)
	return simpleSerie


serie = serieWithNan()
serie.name = "Random Numbers"
serie.index.name = "Index"
print(serie)