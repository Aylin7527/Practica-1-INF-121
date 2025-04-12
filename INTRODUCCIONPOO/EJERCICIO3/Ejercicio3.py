class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad

    def acelerar(self):
        self.__velocidad += 10
        print(f"{self.__marca} {self.__modelo} acelera. Nueva velocidad: {self.__velocidad} km/h")

    def frenar(self):
        self.__velocidad -= 5
        if self.__velocidad < 0:
            self.__velocidad = 0
        print(f"{self.__marca} {self.__modelo} frena. Nueva velocidad: {self.__velocidad} km/h")

    def mostrar_velocidad(self):
        print(f"El coche {self.__marca} {self.__modelo} va a {self.__velocidad} km/h")

coche1 = Coche("Toyota", "Corolla", 50)
coche2 = Coche("Ford", "Focus", 30)

coche1.acelerar()
coche1.frenar()
coche1.mostrar_velocidad()

coche2.acelerar()
coche2.frenar()
coche2.mostrar_velocidad()