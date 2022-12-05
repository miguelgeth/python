def tabla(numero):
    print('Esta es la tabla del ' + str(numero))
    for i in range(1,11):
        print(i*numero)


def run():
    menu = """
VAMOS A VISUALIZAR LAS TABLAS DE MULTIPLICAR
    Selecciona la tabla que quieras ver:
        2. tabla del 2
        3. tabla del 3
        4. tabla del 4
        5. tabla del 5
        6. tabla del 6
        7. tabla del 7
        8. tabla del 8
        9. tabla del 9
            
¿Qué tabla quires ver? Elige una opcion: 
    """
    opcion = int(str(input(menu)))

    if opcion == 2:
        tabla(2)
    elif opcion == 3:
        tabla(3)
    elif opcion == 4:
        tabla(4)
    elif opcion == 5:
        tabla(5)
    elif opcion == 6:
        tabla(6)
    elif opcion == 7:
        tabla(7)
    elif opcion == 8:
        tabla(8)   
    elif opcion == 9:
        tabla(9)                         
    else:
        print('esa no es una opcion')


if __name__ == '__main__':
    run()