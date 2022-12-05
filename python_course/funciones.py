# def print_message():
#     print('Especial message')
#     print('Aprendiendo funciones')


# print_message()

def conversation(message):
    print('Hi')
    print('How are you')
    print(message)# se va a print el parametro que se elija
    print('bye')


option = int(input('Choose an option( 1,2,3): '))
if option == 1:
    conversation('choose 1')
elif option == 2:
    conversation('choose 2')

elif option == 3:
    conversation('choose 3')

else:
    print('choose an option')
