def run():
	mi_diccionario = {# estructura de llaves y valores,accedemos through de sus llaves
	'llave1':1,
	'llave2':2,
	'llave3':3,
	}
	print(mi_diccionario)
	print(mi_diccionario['llave1'])
	print(mi_diccionario['llave2'])
	print(mi_diccionario['llave3'])

	poblacion_paises = {
		'argentina': 45000000,
		'brasil': 200000000,
		'colombia': 50000000,
	}
	print(poblacion_paises['argentina'])


	for pais in poblacion_paises.keys():#metodo para traer las llaves
		print(pais)


	for pais in poblacion_paises.values:# los valores
		print(pais)


	for pais,poblacion in poblacion_paises.items:# los dos
		print(f'{pais} tiene {poblacion} habitantes')


if __name__ == '___main__':
	run()