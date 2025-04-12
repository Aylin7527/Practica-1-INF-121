class Celular:
    def __init__(self, aplicaciones, espacioDisponible, maxDisponibles, bateria):
        self.__aplicaciones = aplicaciones
        self.__espacioDisponible = espacioDisponible
        self.__maxAplicaciones = maxDisponibles
        self.__bateria = bateria

    def configurar(self, espacio: int, max_apps: int, bateria: float):
        self.__espacioDisponible = espacio
        self.__maxAplicaciones = max_apps
        self.__bateria = bateria

    def instalarAplicacion(self, nombre: str, tamano: int):
        if len(self.__aplicaciones) < self.__maxAplicaciones and tamano <= self.__espacioDisponible:
            self.__aplicaciones.append((nombre, tamano))
            self.__espacioDisponible -= tamano
            print(f"Aplicación {nombre} instalada.")
        else:
            print(f"No se puede instalar {nombre}. Espacio insuficiente o límite alcanzado.")

    def usarAplicacion(self, nombre: str, minutos: int):
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

    def mostrarBateria(self):
        print(f"Batería restante: {self.__bateria}%")

cel = Celular([], 0, 0, 0)
cel.configurar(1024, 20, 100.0)

cel.instalarAplicacion("WhatsApp", 120)
cel.instalarAplicacion("Facebook", 300)
cel.instalarAplicacion("Notas", 50)

cel.usarAplicacion("WhatsApp", 6000)
cel.usarAplicacion("Facebook", 8000)
cel.usarAplicacion("Notas", 6000)
cel.usarAplicacion("Facebook", 5000)
cel.usarAplicacion("WhatsApp", 7000)
cel.usarAplicacion("Notas", 4000)

cel.mostrarBateria()
