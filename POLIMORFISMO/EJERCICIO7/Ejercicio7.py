class Perro:
    def __init__(self, nombre, edad, raza):
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza

    def hacerSonido(self):
        print(f"{self.__nombre} hace: ¡Woof! ¡Woof!")

    def moverse(self):
        print(f"{self.__nombre} corre.")

class Gato:
    def __init__(self, nombre, edad, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__color = color

    def hacerSonido(self):
        print(f"{self.__nombre} hace: ¡Miau! ¡Miau!")

    def moverse(self):
        print(f"{self.__nombre} salta.")

class Pajaro:
    def __init__(self, nombre, edad, tipo):
        self.__nombre = nombre
        self.__edad = edad
        self.__tipo = tipo

    def hacerSonido(self):
        print(f"{self.__nombre} hace: ¡Kraa! ¡Kraa!")

    def moverse(self):
        print(f"{self.__nombre} vuela.")

perro = Perro("Snoopy", 3, "Beagle")
gato = Gato("Garfield", 2, "Naranja")
pajaro = Pajaro("Blue", 1, "Guacamayo de Spix")

perro.hacerSonido()
perro.moverse()

gato.hacerSonido()
gato.moverse()

pajaro.hacerSonido()
pajaro.moverse()