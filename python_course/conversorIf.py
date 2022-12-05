menu = '''
Welcome to currency converter 💰

1- Pesos Colombianos
2- Pesos chilenos
3- Pesos mexicanos

Choose an option: '''

option = int(input(menu))
if option == 1:
    pesos = input('cuantos pesos colombianos tienes? :')
    pesos = float(pesos)
    dollar_value = 4000
    convert = pesos / dollar_value
    convert = round(convert, 2)
    convert = str(convert)
    print(f'You have {convert} dollars')


elif option == 2:
    pesos = input('cuantos pesos argentinos tienes? :')
    pesos = float(pesos)
    dollar_value = 65
    convert = pesos / dollar_value
    convert = round(convert, 2)
    convert = str(convert)
    print(f'You have {convert} dollars')

elif option == 3:
    pesos = input('cuantos pesos mexicanos tienes? :')
    pesos = float(pesos)
    dollar_value = 24
    convert = pesos / dollar_value
    convert = round(convert, 2)
    convert = str(convert)
    print(f'You have {convert} dollars')

else:
    print('Enter any right option, please')