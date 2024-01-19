#!/usr/bin/python3
import unittest
from greedy_algorithm import *


class TestOptimalidad(unittest.TestCase):

    def test_3_elems(self):
        lista_tiempos = get_lists_from_csv('archivos_prueba/3elem.csv')
        _, tiempo = obtener_orden_y_tiempo_optimo_de_videos(lista_tiempos)
        self.assertEqual(tiempo, 10)

    def test_10_elems(self):
        lista_tiempos = get_lists_from_csv('archivos_prueba/10elem.csv')
        _, tiempo = obtener_orden_y_tiempo_optimo_de_videos(lista_tiempos)
        self.assertEqual(tiempo, 29)

    def test_100_elems(self):
        lista_tiempos = get_lists_from_csv('archivos_prueba/100elem.csv')
        _, tiempo = obtener_orden_y_tiempo_optimo_de_videos(lista_tiempos)
        self.assertEqual(tiempo, 5223)

    def test_10000_elems(self):
        lista_tiempos = get_lists_from_csv('archivos_prueba/10000elem.csv')
        _, tiempo = obtener_orden_y_tiempo_optimo_de_videos(lista_tiempos)
        self.assertEqual(tiempo, 497886735)


def get_lists_from_csv(file_name):
    ret_list = []
    with open(file_name, 'r') as f:
        for line in f:
            s, a = line.split(',')
            ret_list.append((int(s), int(a)))
    return ret_list


if __name__ == '__main__':
    unittest.main()
