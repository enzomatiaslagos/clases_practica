#ejercicio 9.2 a)
def contar_palabras(texto):
	diccionario = {}
	lista_palabras= texto.split()
	for palabra in lista_palabras:
		if palabra not in diccionario:
			diccionario[palabra] = 1
		else:
			diccionario[palabra] += 1
	return diccionario
def contar_2(texto):#ineficiente
	diccionario = {}#ineficiente
	lista_palabras= texto.split()#ineficiente
	for palabra in lista_palabras:#ineficiente
		diccionario[palabra] = lista_palabras.count(palabra)#ineficiente
	return diccionario#ineficiente
print(contar_2("la la la banda loca loca loca de ricotti"))
print(contar_palabras("la la la banda loca loca loca de ricotti"))
def contar_3(texto):
	diccionario = {}
	lista_palabras= texto.split()
	for palabra in lista_palabras:
		dic[palabra] = dic.get(palabra,0)+1
	return diccionario
#ejercicio 9.2 b)
def contar_caracteres(cadena):
	diccionario = {}
	for letra in cadena:
		diccionario[letra] = diccionario.get(letra,0) + 1
	return diccionario
#si quisieramos imprimir el diccionario ordenado de la funcion de arriba
def imprimir_diccionario_ordenado_1(diccionario):
	lista_ordenada = list(diccionario)
		print sorted(lista_ordenada)
def imprimir_diccionario_ordenado_2(diccionario):
	lista_ordenada = sorted(list(diccionario))
	print lista_ordenada
#si quisiera imprimir el diccionario ordenado de acuerdo a un parametro que quiera
def imprimir_diccionario_ordenado_condicion(diccionario):
	diccionario = {}
	for clave, valor in sorted(diccionario.items(), key = lambda x:x[1])
		print(clave,valor)
#hacer el inciso c de tarea
#9.4 (escribir una funcion que reciba un texto y para 
#cada caracter devuelva la cadena mas larga en la que se encuentra ese caracter)
#ejemplo "hola que tal" a---> "hola"
def ejercicio94 (texto):
	diccionario ={}
	for palabra in texto.split():
		for caracter in palabra:
			if not diccionario.get(caracter,False):
				diccionario[caracter] = palabra
			elif len(palabra) > len(diccionario[caracter])
				diccionario[caracter] = palabra
	return diccionario
def ejercicio9_4_por_el_profesor(cadena):
	diccionario = {}
	for palabra in cadena.split():
		for caracter in palabra:
			if diccionario.get(caracter):
				if len(palabra) > len(diccionario[caracter])
					diccionario[caracter] = palabra
				else :
					diccionario[caracter] = palabra
	return diccionario
