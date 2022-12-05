def is_prime(number):# all of this is for prime numbers
	counter = 0
	
	for i in range(1,number + 1):# i es el que itera, entonces iniciamos desde 1 hasta el number que se diga +1
		if i == 1 or i == number:
			continue #lo que entendi si i == 1 or i == number: nos saltamos ese numero, en este caso los que nos son primos, entonces nos saltamos esal vuelta y i ya nos vale abajo 2
		if number % i == 0:# para identificar los no primos,, etnonces i=2 % no da 0 por lo tanto no se aumenta el counter y nos va True abajo
			counter += 1
	if counter == 0:# si esto es 0 significa que son prime y me da true
		return True
	else:
		return False


def run():
	number = int(input('Type a number: '))
	if is_prime(number):
		print('its prime')
	else: 
		print('it is no prime')


if __name__ == '__main__':
	run()