import random# importar el modulo random, que maneja numeros randoms: un modulo es practicamente codigo de otros

def password_generator():
	mayus = ['A','B','C','D','E','F','G']
	min = ['a','b','c','d','e','f','g']
	symbol = ['@','#','$','!','%','&']
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	
	caracteres = mayus + min + symbol + numbers
	

	password = []

	for i in range(15):# por cada ciclo elige uno al azar
		caracter_random = random.choice(caracteres)# choice funcion especial del modulo random,elije el caracter al azar
		password.append(caracter_random)

	password = ''.join(password)# trasnform a list to a str
	return password


def run():
	password = password_generator()
	print(f'Your passwords is: {password} ')

if __name__ == '__main__':
	run()