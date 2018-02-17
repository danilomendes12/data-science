######################### filtros usando filter

list = range(10)

test_list = [
"hello",
"x,y,z. i like this.",
"this is two xx",
"this, x, here x is, here it is againx"
]

def is_par(num):
	if(num % 2 == 0):
		return True
	else:
		return False

def tem_x(my_string):
    return my_string.count("x") >= 2

#cria uma lista de booleanos se o numero for par
boolean_list = map(is_par, list)

#cria uma lista só com número par
filtered_list = filter(is_par, list)

#filtra string
filtered_string_list = filter(tem_x,test_list)

for item in filtered_string_list:
	print(item)

