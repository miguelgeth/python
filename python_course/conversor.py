# ENT LAS OPERAECIONES TOCA PENSARLAS BIEN , HACERLO COHERENTE

pesos = input('cuantos pesos colombianos tienes? :')
pesos = float(pesos)
dollar_value = 4000
convert = pesos / dollar_value
convert = round(convert, 2)# para que me salgan solo 2 decimales
convert = str(convert)# lo pasamos a string porque no podemos concatenar float, solo podemos str
# print('You have  $' + convert + ' dollars')
print(f'You have {convert} dollars')


# podemos hacer todo esto junto

# convert from COl to bitcoin
cop = input('How many COP do you have?')
cop = float(cop)
bitcoin_value = 124708970
convertCop = cop / bitcoin_value
convertCop = round(convertCop, 5)
convertCop = str(convertCop)
print(f'You have {convertCop} bitcoins')

# dollar to COP
dollar = input('How many dollars do you have? : ')
dollar = float(dollar)
cop_value = 4000
convertDollar =  cop_value * dollar
convertDollar = str(convertDollar)
print(f'You have {convertDollar} COP')



#convert from BTC to COP, me funciona kinda good el problema es pasar de btc a cop
btc = input('How many Btc do you have? : ')
btc = float(btc)
cop_value = 1250000
convertBtc = btc * cop_value
# convertBtc = round(convertBtc,4)
convertBtc = float(convertBtc)
convertBtc = str(convertBtc)
print(f'You have {convertBtc} COP')