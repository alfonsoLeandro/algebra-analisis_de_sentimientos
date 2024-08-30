class Frase:
    qnt_palabras = 0

    def __init__(self, frase, qnt_palabras):
        Frase.qnt_palabras = qnt_palabras
        self.frase = frase
        self.s = [0, 0, 0]
        self.w = []
        for i in range(qnt_palabras):
            self.w.append(0)
        self.calidad = 0
        self.promedio_sentimiento = 0


    def calcular_calidad(self):
        sum_w = sum(self.w)
        self.calidad = sum_w / Frase.qnt_palabras

    def calcular_promedio_sentimiento(self):
        ps = [1, 0, -1]
        for i in range(3):
            self.promedio_sentimiento += ps[i] * self.s[i]

    def __str__(self):
        return f"frase: {self.frase}, s: {self.s}, w: {self.w}, calidad: {self.calidad}, promedio_sentimiento: {self.promedio_sentimiento}"