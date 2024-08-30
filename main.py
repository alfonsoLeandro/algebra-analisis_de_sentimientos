from enum import Enum

from Frase import Frase

from pandas import pandas as pd


class Calidad(Enum):
    BUENO = 1
    NEUTRAL = 0
    MALO = -1


qualityPerPalabra = []
def llenar_palabras():
    qualityPerPalabra.append({
        "palabra": "bueno",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "buenos",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "buena",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "buenas",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "bonito",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "bonitos",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "bonita",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "bonitas",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "lindo",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "lindos",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "genial",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "empanada",
        "calidad": Calidad.BUENO
    })
    qualityPerPalabra.append({
        "palabra": "bien",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "normal",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "normales",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "tibio",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "tranquilo",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "tranquila",
        "calidad": Calidad.NEUTRAL
    })
    qualityPerPalabra.append({
        "palabra": "refunfuñante",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "horrible",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "horribles",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "miedo",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "muerte",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "escapar",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "malo",
        "calidad": Calidad.MALO
    })
    qualityPerPalabra.append({
        "palabra": "mal",
        "calidad": Calidad.MALO
    })


def generar_frases():
    qnt_palabras = len(qualityPerPalabra)

    return {
        1: Frase(
            "El paisaje del atardecer era genial, con colores lindos y un ambiente tranquilo que hacía que todo pareciera bueno",
            qnt_palabras),
        2: Frase(
            "Aunque la película tenía momentos normales, la actuación principal fue refunfuñante y dejó a todos con un mal sabor",
            qnt_palabras),
        3: Frase(
            "La decoración de la fiesta era bonita, con luces brillantes y detalles lindos que hacían sentir a todos bien y tranquilos",
            qnt_palabras),
        4: Frase(
            "El día comenzó normal, pero se volvió horrible cuando la tormenta trajo consigo una sensación de miedo y la necesidad de escapar",
            qnt_palabras),
        5: Frase(
            "La charla fue buena y genial, aunque algunos comentarios neutrales no aportaron mucho, el ambiente en general fue tranquilo",
            qnt_palabras),
        6: Frase(
            "La casa estaba decorada de manera linda, con un toque bonito en cada rincón, lo que hizo que todos se sintieran bien y acogidos",
            qnt_palabras),
        7: Frase(
            "A pesar de que el clima estaba normal, el paseo por el bosque se volvió horrible al escuchar ruidos que causaban miedo y nos hicieron querer escapar",
            qnt_palabras),
        8: Frase(
            "La comida en el restaurante fue genial, desde las empanadas hasta el postre, todo estaba bueno, lo que hizo que la noche fuera tranquila",
            qnt_palabras),
        9: Frase(
            "Aunque la reunión fue neutra y la mayoría de las personas estuvieron tibias, hubo algunos momentos que se sintieron refunfuñantes",
            qnt_palabras),
        10: Frase(
            "El viaje fue bueno al principio, pero se tornó malo cuando nos perdimos en una zona horrible y sentimos la necesidad de escapar",
            qnt_palabras),
        11: Frase(
            "La fiesta tuvo un ambiente genial, con música buena y una decoración bonita que hizo que todos se sintieran lindos y bien",
            qnt_palabras),
        12: Frase(
            "La película era normal al principio, pero se volvió horrible hacia el final, dejando una sensación de miedo en todos",
            qnt_palabras),
        13: Frase(
            "Aunque el ambiente en la cafetería era tranquilo, el servicio fue tibio y dejó a algunos clientes refunfuñantes",
            qnt_palabras),
        14: Frase(
            "La mañana comenzó buena, con un cielo lindo y un ambiente tranquilo, pero se volvió malo cuando llegó una noticia horrible",
            qnt_palabras),
        15: Frase(
            "La cena fue genial, con platos buenos y bonitos que hicieron que la noche fuera tranquila y agradable para todos",
            qnt_palabras),
        16: Frase(
            "bueno bueno bueno bueno bueno",
            qnt_palabras)
    }



def procesar_frases(frases):
    qnt_palabras = len(qualityPerPalabra)

    for fraseId in frases:
        palabras = list(frases[fraseId].frase.lower().split(" "))
        for i in range(qnt_palabras):
            if palabras.__contains__(qualityPerPalabra[i]['palabra']):
                frases[fraseId].w[i] = 1
                match qualityPerPalabra[i]['calidad']:
                    case Calidad.BUENO:
                        frases[fraseId].s[0] += 1
                    case Calidad.NEUTRAL:
                        frases[fraseId].s[1] += 1
                    case Calidad.MALO:
                        frases[fraseId].s[2] += 1
        frases[fraseId].calcular_calidad()
        frases[fraseId].calcular_promedio_sentimiento()




llenar_palabras()

if __name__ == "__main__":
    frases = generar_frases()
    procesar_frases(frases)
    pd.DataFrame({
        "frase": [frase.frase for frase in frases.values()],
        "calidad": [frase.calidad for frase in frases.values()],
        "promedio_sentimiento": [frase.promedio_sentimiento for frase in frases.values()],
    }).to_csv("frases.csv")
