list = range(10)

def cubo(num):
	return num ** 3

def is_par(num):
	if(num % 2 == 0):
		return True
	else:
		return False

#cria lista nova com o cubo dos valores
cube_list = [item**3 for item in list]

#cria lista nova apenas com os pares
even_list = [item for item in list if item % 2 == 0]

#cria lista nova com o cubo dos pares
cubed = [cubo(item) for item in list if is_par(item)]

print(cubed)




