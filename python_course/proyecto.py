def calculator(num1,num2):
	num1 = float(input('Type a number'))
	num2 = float(input('Type a number'))
	numbers = num1 + num2
	return numbers
	print(calculator(num1,num2))


menu = '''
calculator
choose one option:

1- sum
2- rest
'''


def run():
	# operation = calculator(nu)
	option = int(input(menu))
	if option == 1:
		print(f'You chose sum: {calculator(num1,num2)}')
	elif option ==2:
		print(f'You chose rest: {calculator}')
	else:
		print('Chooe one option:')


# if __name__ == '__main__':
# 	run()