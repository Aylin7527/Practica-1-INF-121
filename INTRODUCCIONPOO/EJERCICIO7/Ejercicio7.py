class Celular:
    def __init__(self, aplicaciones, espacioDisponible, maxDisponibles, bateria):
        self.__aplicaciones = aplicaciones
        self.__espacio_disponible = espacioDisponible
        self.__max_aplicaciones = maxDisponibles
        self.__bateria = bateria

    def configurar(self, espacio: int, max_apps: int, bateria: float):
        self.__espacio_disponible = espacio
        self.__max_aplicaciones = max_apps
        self.__bateria = bateria

    def instalar_aplicacion(self, nombre: str, tamano: int):
        if len(self.__aplicaciones) < self.__max_aplicaciones and tamano <= self.__espacio_disponible:
            self.__aplicaciones.append((nombre, tamano))
            self.__espacio_disponible -= tamano
            print(f"Aplicación {nombre} instalada.")
        else:
            print(f"No se puede instalar {nombre}. Espacio insuficiente o límite alcanzado.")

    def usar_aplicacion(self, nombre: str, minutos: int):
        if self.__bateria <= 0:
            print("Celular apagado")
            return

        for app in self.__aplicaciones:
            if app[0] == nombre:
                tamano = app[1]
                if tamano > 250:
                    consumo = 0.05
                elif tamano > 100:
                    consumo = 0.02
                else:
                    consumo = 0.01

                bateria_usada = consumo * (minutos / 10)
                self.__bateria -= bateria_usada
                self.__bateria = max(self.__bateria, 0)
                self.__bateria = round(self.__bateria, 2)

                if self.__bateria == 0:
                    print("Celular apagado")
                else:
                    print(f"Usando {nombre}. Batería actual: {self.__bateria}%")
                return

        print("Aplicación no encontrada.")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.__bateria}%")

cel = Celular([], 0, 0, 0)
cel.configurar(1024, 20, 100.0)

cel.instalar_aplicacion("WhatsApp", 120)
cel.instalar_aplicacion("Facebook", 300)
cel.instalar_aplicacion("Notas", 50)

cel.usar_aplicacion("WhatsApp", 6000)
cel.usar_aplicacion("Facebook", 8000)
cel.usar_aplicacion("Notas", 6000)
cel.usar_aplicacion("Facebook", 5000)
cel.usar_aplicacion("WhatsApp", 7000)
cel.usar_aplicacion("Notas", 4000)

cel.mostrar_bateria()