class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.__edad = edad
        self.__ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.__nombre} de {self.__ciudad}")

    def esMayorDeEdad(self):
        return self.__edad >= 18

p1 = Persona("Juan", 20, "La Paz")
p2 = Persona("María", 17, "Cochabamba")
p3 = Persona("Luis", 25, "Santa Cruz")

p1.saludar()
print(f"Mayor de edad: {p1.esMayorDeEdad()}")
p2.saludar()
print(f"Mayor de edad: {p2.esMayorDeEdad()}")
p3.saludar()
print(f"Mayor de edad: {p3.esMayorDeEdad()}")