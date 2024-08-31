from Calidad import Calidad


class Palabra:
    qnt_palabras = 0

    def __init__(self, palabra: str, calidad: Calidad):
        self.palabra = palabra
        self.calidad = calidad

    def __str__(self):
        return f"Palabra: {self.palabra}, calidad: {self.calidad}"
