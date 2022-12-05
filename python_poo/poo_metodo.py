class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):# para definir la distancia usamos el metodo eucliniano
        x_diff = (self.x - otra_coordenada.x)**2# cual es la distancia entre una x y otra_coordenada su x y la tenemos al squared
        y_diff = (self.y - otra_coordenada.y)**2# lo mismo
        return(x_diff + y_diff)**0.5 #para elevarlo a una raiz cuadrado, por eso se ponia asi la raiz en la clase que list comprehension


if __name__ == '__main__':
    coord_1 = Coordenada(3,30)# coordenada de la primera instancia
    coord_2 = Coordenada(4,8)# coordenada 2
    print(coord_1.distancia(coord_2))# para saber la distancia entre las coordenadas
    print(isinstance(coord_2, Coordenada))# para si alguna de nuestra coord_2 es instancia de Coordenada y nos data True or False