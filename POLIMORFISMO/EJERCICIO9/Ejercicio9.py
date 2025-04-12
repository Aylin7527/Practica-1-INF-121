class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self.__capacidad = capacidad
        self.__resistencia = resistencia
        self.__tipo = tipo

    def accion(self):
        print(f"El {self.__tipo} está siendo abierto y se pueden acceder a sus objetos.")

    def colocar(self, orientacion):
        print(f"Colocando el {self.__tipo} en la orientacion: {orientacion}")

    def romper(self):
        print(f"El {self.__tipo} está siendo roto. Los objetos dentro pueden caerse y perderse.")

class BloqueTnt:
    def __init__(self, tipo, daño):
        self.__tipo = tipo
        self.__daño = daño

    def accion(self):
        print(f"El {self.__tipo} está encendido y listo para explotar.")

    def colocar(self, orientacion):
        print(f"Colocando el {self.__tipo} en la orientacion: {orientacion}")

    def romper(self):
        print(f"¡BOOM! El {self.__tipo} ha explotado causando {self.__daño} de daño.")

class BloqueHorno:
    def __init__(self, color, capacidadComida):
        self.__color = color
        self.__capacidadComida = capacidadComida

    def accion(self):
        print(f"El {self.__color} horno está cocinando comida con capacidad de {self.__capacidadComida} unidades.")

    def colocar(self, orientacion):
        print(f"Colocando el {self.__color} horno en la orientacion: {orientacion}")

    def romper(self):
        print(f"El {self.__color} horno está siendo roto. Se perderá la comida si está en proceso.")

bloqueCofre1 = BloqueCofre(30, 100, "Cofre")
bloqueCofre2 = BloqueCofre(50, 150, "Cofre")
bloqueTnt1 = BloqueTnt("TNT", 100)
bloqueTnt2 = BloqueTnt("TNT", 120)
bloqueHorno1 = BloqueHorno("Rojo", 20)
bloqueHorno2 = BloqueHorno("Azul", 25)

bloqueCofre1.accion()
bloqueCofre1.colocar("Suelo")
bloqueCofre1.romper()

bloqueCofre2.accion()
bloqueCofre2.colocar("Pared")
bloqueCofre2.romper()

bloqueTnt1.accion()
bloqueTnt1.colocar("Techo")
bloqueTnt1.romper()

bloqueTnt2.accion()
bloqueTnt2.colocar("Suelo")
bloqueTnt2.romper()

bloqueHorno1.accion()
bloqueHorno1.colocar("Suelo")
bloqueHorno1.romper()

bloqueHorno2.accion()
bloqueHorno2.colocar("Pared")
bloqueHorno2.romper()