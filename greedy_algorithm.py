#!/usr/bin/python3

def obtener_orden_y_tiempo_optimo_de_videos(tiempos: list[tuple[int, int]]):
    orden_optimo = sorted(tiempos, key=lambda tiempo: tiempo[1], reverse=True)

    finalizacion_anterior_scaloni = 0
    finalizacion_anterior_ayudante = 0

    for tiempo_scaloni, tiempo_ayudante in orden_optimo:
        finalizacion_scaloni = finalizacion_anterior_scaloni + tiempo_scaloni
        finalizacion_ayudante = finalizacion_scaloni + tiempo_ayudante

        finalizacion_anterior_scaloni = finalizacion_scaloni

        if finalizacion_anterior_ayudante < finalizacion_ayudante:
            finalizacion_anterior_ayudante = finalizacion_ayudante

    return orden_optimo, finalizacion_anterior_ayudante
