planets = ["Mercury","Venues","Earth", "Mars"]
for planet in planets:
    print(planet, end="")# end lo qeu hace es que me los pone pegados y sin end es tipo lista de cosas

squares = []

for n in range(1,11):
    squares.append(n)
print(squares)#fuera del bloque de codigo(for) y print(squares) porque queremos pasarle el ciclo for a la lista vacia, si print(n) me muestra el ciclo normal, pero como quiero pasarle esos elementos a mis list vacia pues lo hago asi

li = ["Miguel","juan","camila"]
def hola(student):
    return f"hola {student}"

for student in li:
    print(hola(student))






