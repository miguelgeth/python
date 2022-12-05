
def convert(pesos_type,dollar_value):
    pesos = input(f'cuantos pesos {pesos_type} tienes? :')
    pesos = float(pesos)
    convert = pesos / dollar_value
    convert = round(convert, 2)
    convert = str(convert)
    print(f'You have {convert} dollars')


menu = '''
Welcome to currency converter 💰

1- Pesos Colombianos
2- Pesos chilenos
3- Pesos mexicanos

Choose an option: '''
option = int(input(menu))
if option == 1:
    convert('COP',4000)
elif option == 2:
    convert('ARG', 65)
elif option == 3:
    convert('MEX', 24)
else:
    print('Please choose an option')