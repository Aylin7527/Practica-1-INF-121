class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = nota1
        self.__nota2 = nota2

    def calcularPromedio(self):
        return (self.__nota1 + self.__nota2) / 2

    def aprobo(self):
        return self.calcularPromedio() >= 6

    def mostrarPromedios(self):
        print(f"Estudiante: {self.__nombre}")
        print(f"Promedio: {self.calcularPromedio()}")
        print("¿Aprobó?: " + ("Sí" if self.aprobo() else "No"))

est1 = Estudiante("Juan", 7, 8)
est2 = Estudiante("Ana", 5, 6)
est3 = Estudiante("Luis", 4, 5)

est1.mostrarPromedios()
est2.mostrarPromedios()
est3.mostrarPromedios()