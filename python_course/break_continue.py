def run():
	for i in range(1000):
		if i % 2 != 0:# if i divide 2 el resto es != 0 no vamos a print porque es impar y solo queremos print pares
			continue
		print(i)

	for i in range(1000):
		if i == 55:
			break
		print(i)

	text = input('Type a text: ')
	for i in text:
		if i == 'o':
			break
		print(i)


# while
	LIMIT = 1000
	counter = 2
	while counter < LIMIT:
		if counter %2 != 0:
			continue# nos saltamos ese numero que en este caso serian los impares, porque esos numeros si son distntos a 0
		counter += 2
		print(counter)

	LIMIT = 1000
	counter = 0
	while counter < LIMIT:
		if counter == 60:
			break# poner contniue aca funciona porque siempre se va a cumplir entonces da igual
		counter += 1
		print(counter)



if __name__ =='__main__':
	run()