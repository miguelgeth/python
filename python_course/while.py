def run():
	LIMITE = 1000
	counter = 0
	power_2 = 2**counter

	while power_2 < LIMITE:
		print(f'2 raised to {counter} its equal to {power_2}')
		counter = counter + 1
		power_2 = 2**counter




if __name__ == '__main__':
	run()
