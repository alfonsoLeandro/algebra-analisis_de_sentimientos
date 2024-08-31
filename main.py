from Calidad import Calidad
from Frase import Frase

from pandas import pandas as pd

from Palabra import Palabra

qualityPerPalabra = []


def llenar_palabras():
    qualityPerPalabra.append(Palabra("beneficiado", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("bien", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("buena", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("deliciosa", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("especialmente", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("espectacular", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("excelente", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("gane", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("genial", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("gusta", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("gusto", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("inteligente", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("juega", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("jugar", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("jugue", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("lindo", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("nobel", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("recomiendo", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("solucion", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("sorprende", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("suerte", Calidad.BUENO))
    qualityPerPalabra.append(Palabra("super", Calidad.BUENO))

    qualityPerPalabra.append(Palabra("demasiado", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("gran", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("mames", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("mas", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("merece", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("melancolico", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("no", Calidad.NEUTRAL))
    qualityPerPalabra.append(Palabra("puro", Calidad.NEUTRAL))

    qualityPerPalabra.append(Palabra("aburrio", Calidad.MALO))
    qualityPerPalabra.append(Palabra("asco", Calidad.MALO))
    qualityPerPalabra.append(Palabra("decepcion", Calidad.MALO))
    qualityPerPalabra.append(Palabra("demonio", Calidad.MALO))
    qualityPerPalabra.append(Palabra("depravado", Calidad.MALO))
    qualityPerPalabra.append(Palabra("desesperante", Calidad.MALO))
    qualityPerPalabra.append(Palabra("disociada", Calidad.MALO))
    qualityPerPalabra.append(Palabra("exponerlo", Calidad.MALO))
    qualityPerPalabra.append(Palabra("expuesto", Calidad.MALO))
    qualityPerPalabra.append(Palabra("innecesario", Calidad.MALO))
    qualityPerPalabra.append(Palabra("miserable", Calidad.MALO))
    qualityPerPalabra.append(Palabra("nunca", Calidad.MALO))
    qualityPerPalabra.append(Palabra("pego", Calidad.MALO))
    qualityPerPalabra.append(Palabra("pierden", Calidad.MALO))
    qualityPerPalabra.append(Palabra("problema", Calidad.MALO))
    qualityPerPalabra.append(Palabra("quemarlo", Calidad.MALO))
    qualityPerPalabra.append(Palabra("retirado", Calidad.MALO))
    qualityPerPalabra.append(Palabra("reclamar", Calidad.MALO))
    qualityPerPalabra.append(Palabra("triste", Calidad.MALO))
    qualityPerPalabra.append(Palabra("verguenza", Calidad.MALO))


def generar_frases():
    """
    Obtuvimos frases al azar de comentarios de publicaciones en twitter (X).
    """
    qnt_palabras = len(qualityPerPalabra)

    return {
        1: Frase(
            "ES REALMENTE ESPECTACULAR",
            qnt_palabras),
        2: Frase(
            "a mi toco marcar a uno que hizo inferiores en river en los '90, yo le sacaba años de diferencia, "
            "que van a ser los que me va a tocar recuperarme del baile que me pego",
            qnt_palabras),
        3: Frase(
            "una vez jugue con un arquero del america de Mexico, ya retirado, no le pudimos meter un gol nunca, "
            "al rato, el flaco se aburrio y pidio cambiar, se puso a jugar de 9, nos metio como 40 goles...",
            qnt_palabras),
        4: Frase(
            "Jugue con alguien q andaba en las inferiores de Ferro, es demasiado notorio cuando uno se dedica a "
            "ser futbolista con alguien que lo juega como hobby, de suerte le gane un par de duelos",
            qnt_palabras),
        5: Frase(
            "ufff cuanta razon no me habia dado cuenta que genial, que inteligente se merece el nobel que gran"
            " descubrimiento...  yo pensaba que el agua NACE en las botellas hijole que decepción ufff no mames"
            " que increible waooo es tan científica esta publicación que no puedo hacer mas que dejar de "
            "seguir esta pagina tan científica y sobre todooo inteligente.",
            qnt_palabras),
        6: Frase(
            "El punto es que el agua embotellada es un negocio innecesario",
            qnt_palabras),
        7: Frase(
            "Asi es como de disociada tienen la realidad las mujeres en España especialmente la Charo que"
            " dice no me lo creo , es desesperante no hay solucion",
            qnt_palabras),
        8: Frase(
            "El problema es que han lavado tanto el cerebro a la gente con que la izquierda es buena para el"
            " pueblo y la derecha es el demonio que por eso les sorprende, demuestra que ni se han informado por"
            " otras vias o leyendo el programa electoral",
            qnt_palabras),
        9: Frase(
            "Bien hecho, grabarlo en el momento, dejarlo a las autoridades, exponerlo y quemarlo toda su"
            " miserable vida. Eso vale mas que paloterapia, con paloterapia hasta sale beneficiado,"
            " puro depravado esta siendo expuesto",
            qnt_palabras),
        10: Frase(
            "Muy lindo la verdad, me gusto Me gusta ese ambiente un tanto triste (???) o melancólico..."
            " No sabría explicarlo que le dan.",
            qnt_palabras),
        11: Frase(
            "Un asco la pizza fina como nunca y encima llamas para reclamar y la respuesta del encargado y "
            "mismo dueño del lugar es que hay días que la pizza sale así y que a algunos clientes les gusta así!"
            " Muy fuertee!!! Nunca más . Otro cliente que pierden porque ya conozco varios !",
            qnt_palabras),
        12: Frase(
            "Pedí pasta y estaba deliciosa super recomiendo, las personas q fueron conmigo pidieron sanguche "
            "caliente, lasaña y Pamplona con papas y también dijeron q excelente, los precios muy bien acorde al "
            "tamaño de las porciones. Volveremos …",
            qnt_palabras),
        13: Frase(
            "no entiendo como en montevideo no hay un solo delivery de tortas fritas, somos una VERGÜENZA",
            qnt_palabras)
    }


def procesar_frases(frases):
    qnt_palabras = len(qualityPerPalabra)

    for fraseId in frases:
        palabras = list(frases[fraseId].frase.split(" "))
        for i in range(qnt_palabras):
            if palabras.__contains__(qualityPerPalabra[i].palabra):
                frases[fraseId].w[i] = 1
                match qualityPerPalabra[i].calidad:
                    case Calidad.BUENO:
                        frases[fraseId].s[0] += 1
                    case Calidad.NEUTRAL:
                        frases[fraseId].s[1] += 1
                    case Calidad.MALO:
                        frases[fraseId].s[2] += 1
        frases[fraseId].calcular_calidad()
        frases[fraseId].calcular_promedio_sentimiento()


def analizar_frases_generadas():
    frases = generar_frases()
    procesar_frases(frases)
    table = pd.DataFrame({
        "frase": [frase.frase for frase in frases.values()],
        "calidad": [frase.calidad for frase in frases.values()],
        "promedio_sentimiento": [frase.promedio_sentimiento for frase in frases.values()],
    })
    table.sort_values(by=['promedio_sentimiento'], ascending=False, inplace=True)
    print(table)


llenar_palabras()

if __name__ == "__main__":
    analizar_frases_generadas()
