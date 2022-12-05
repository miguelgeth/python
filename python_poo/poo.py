class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    cualquier_nombre = Persona("Miguel Garcia", 20)
    persona1 = Persona("javier ajsja", 21)
    print(cualquier_nombre.name)
    print(cualquier_nombre.age)


    cualquier_nombre.name = "javier lopez"
    print(cualquier_nombre.name)

    print(persona1.name)
    