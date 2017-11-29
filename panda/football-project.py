import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Objetivo:
#Criar um gráfico simples a partir de uma serie

goals = pd.Series([19,25,15,10,30], index = ["Suarez","Messi","Cristiano Ronaldo","Cavani","Neymar"])

def who_more_goals_than(number_of_goals):
	return goals[goals>number_of_goals]

def who_score_most():
	return goals.max()

def createBarPlot():
	goals.plot(kind="bar")
	plt.show()

def createSortedBarPlot():


createBarPlot()