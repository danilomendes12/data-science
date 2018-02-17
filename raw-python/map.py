
list = range(10)

def cubo(num):
	return num ** 3

#aplica a função na lista toda
new_list = map(cubo, list)

for item in new_list:
	print(item)