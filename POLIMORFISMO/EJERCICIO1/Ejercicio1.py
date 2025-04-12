class Videojuego:
    def __init__(self, nombre, plataforma, cantidadJugadores):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantidadJugadores = cantidadJugadores

    def mostrar(self):
        print(f"Videojuego: {self.__nombre}, Plataforma: {self.__plataforma}, Jugadores: {self.__cantidadJugadores}")

    def agregarJugadores(self, cantidad):
        self.__cantidadJugadores += cantidad
        print(f"Jugadores agregados. Ahora hay {self.__cantidadJugadores} jugadores.")

v1 = Videojuego("FIFA 25", "PS5", 2)
v2 = Videojuego("Minecraft", "PC", 1)

v1.agregarJugadores(1)
v2.agregarJugadores(3)

v1.mostrar()
v2.mostrar()