class Cocinero:
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora

    def sueldoTotal(self):
        return self.__sueldoMes + (self.__horasExtra * self.__sueldoHora)

    def mostrarSueldo(self, sueldo):
        if self.__sueldoMes == sueldo:
            print(f"{self.__nombre}: {self.__sueldoMes}")

class Mesero:
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora
        self.__propina = propina

    def sueldoTotal(self):
        return self.__sueldoMes + (self.__horasExtra * self.__sueldoHora) + self.__propina

    def mostrarSueldo(self, sueldo):
        if self.__sueldoMes == sueldo:
            print(f"{self.__nombre}: {self.__sueldoMes}")

class Administrativo:
    def __init__(self, nombre, sueldoMes, cargo):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__cargo = cargo  

    def sueldoTotal(self):
        return self.__sueldoMes

    def mostrarSueldo(self, sueldo):
        if self.__sueldoMes == sueldo:
            print(f"{self.__nombre} ({self.__cargo}): {self.__sueldoMes}")  

cocinero = Cocinero("Carlos", 2500, 10, 15)
mesero1 = Mesero("Juan", 1200, 5, 10, 200)
mesero2 = Mesero("Maria", 1000, 4, 12, 150)
administrativo1 = Administrativo("Ana", 2000, "Contabilidad")
administrativo2 = Administrativo("Pedro", 2500, "Gerente")

print("Sueldos del Cocinero:", cocinero.sueldoTotal())
print("Sueldos del Mesero 1:", mesero1.sueldoTotal())
print("Sueldos del Mesero 2:", mesero2.sueldoTotal())
print("Sueldos del Administrativo 1:", administrativo1.sueldoTotal())
print("Sueldos del Administrativo 2:", administrativo2.sueldoTotal())

cocinero.mostrarSueldo(2500)
mesero1.mostrarSueldo(1200)
mesero2.mostrarSueldo(1000)
administrativo1.mostrarSueldo(2000)
administrativo2.mostrarSueldo(2500)