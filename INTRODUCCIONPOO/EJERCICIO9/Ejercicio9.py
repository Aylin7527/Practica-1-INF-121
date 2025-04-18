class Computadora:
    def __init__(self, procesador, ram, disco_duro):
        self.__procesador = procesador
        self.__ram = ram
        self.__discoDuro = disco_duro
        self.__encendida = False

    def mostrarComponentes(self):
        print(f"Procesador: {self.__procesador}")
        print(f"RAM: {self.__ram}")
        print(f"Disco Duro: {self.__discoDuro}")

    def encender(self):
        self.__encendida = True
        print("Computadora encendida")

    def apagar(self):
        self.__encendida = False
        print("Computadora apagada")

    def estado(self):
        print("Estado:", "Encendida" if self.__encendida else "Apagada")

pc = Computadora("Intel i7", "16GB", "1TB")
pc.mostrarComponentes()
pc.estado()
pc.encender()
pc.estado()
pc.apagar()
pc.estado()
