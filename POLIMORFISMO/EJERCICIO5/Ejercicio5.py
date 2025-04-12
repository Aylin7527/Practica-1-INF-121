class Oficina:
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.__nroSillas = nroSillas
        self.__nroEscritorios = nroEscritorios
        self.__nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"Oficina: Sillas = {self.__nroSillas}, Escritorios = {self.__nroEscritorios}, Estanterías = {self.__nroEstanterias}")

    def cantidadMuebles(self):
        return self.__nroSillas + self.__nroEscritorios + self.__nroEstanterias

class Aula:
    def __init__(self, nombre, capacidad, nroPupitres):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroPupitres = nroPupitres

    def mostrar(self):
        print(f"Aula: Nombre = {self.__nombre}, Capacidad = {self.__capacidad}, Pupitres = {self.__nroPupitres}")

    def cantidadMuebles(self):
        return self.__nroPupitres

class Laboratorio:
    def __init__(self, nombre, capacidad, nroMesas, nroSillas):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroMesas = nroMesas
        self.__nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio: Nombre = {self.__nombre}, Capacidad = {self.__capacidad}, Mesas = {self.__nroMesas}, Sillas = {self.__nroSillas}")

    def cantidadMuebles(self):
        return self.__nroMesas + self.__nroSillas

oficina1 = Oficina(5, 3, 2)
oficina2 = Oficina(4, 2, 1)
aula1 = Aula("Aula 101", 30, 15)
aula2 = Aula("Aula 102", 25, 12)
laboratorio = Laboratorio("Laboratorio 1", 20, 5, 10)

oficina1.mostrar()
oficina2.mostrar()
aula1.mostrar()
aula2.mostrar()
laboratorio.mostrar()

print("Cantidad de muebles en oficina 1:", oficina1.cantidadMuebles())
print("Cantidad de muebles en oficina 2:", oficina2.cantidadMuebles())
print("Cantidad de muebles en aula 1:", aula1.cantidadMuebles())
print("Cantidad de muebles en aula 2:", aula2.cantidadMuebles())
print("Cantidad de muebles en laboratorio:", laboratorio.cantidadMuebles())
