# -*- coding: utf-8 -*-

import re
import dados.Jugador as j

class Historial:
    def __init__(self, player):
        self.nombre_jugador = player.nombre
        self.archivo = self.abrir_fichero()
        self.numero_partidas = self.cuenta_lineas()
        self.media_pnts = 0
        self.partidas_primero = 0
        self.puesto_medio = 0

    def nombre_jugador(self):
        return self.nombre_jugador


    @property
    def archivo(self):
        return self.archivo


    @property
    def numero_partidas(self):
        return self.numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, value):
        self.numero_partidas = value

    @property
    def media_puntos(self):
        veces=0
        return 2


    @media_puntos.setter
    def media_puntos(self, value):
        self.media_pnts = value

    @property
    def partidas_primero(self):
        texto = self.abrir_fichero()
        return 0

    @partidas_primero.setter
    def partidas_primero(self, value):
        self.partidas_primero = value

    @property
    def puesto_medio(self):
        veces = 0
        texto = self.texto()
        m = re.search('Puesto:\s+(.*?)\n', texto)

        while linea is not None:
            self.puesto_medio += int(m.group(1))
            print(self.puesto_medio)
            linea = self.archivo.readlines()
            veces += 1
        print(self.puesto_medio/veces)
        return 1

    @puesto_medio.setter
    def puesto_medio(self, value):
        self.puesto_medio = value

    def cuenta_lineas(self):
        return len(self.archivo.readlines())

    def abrir_fichero(self):
        try:
            return open("risco_" + self.nombre_jugador + ".txt", "r", encoding="utf-8")
        except FileNotFoundError:
            print("no se ha encontrado el archivo")
            exit(1)

    def texto(self):
        texto_leido = self.archivo.read()
        return texto_leido

    def __str__(self):
        # Comprobar que devuelve los valores bien una vez esté la clase acabada
        return f"\nHistorial de {self.nombre_jugador} " \
               f"\nPartidas hechas → {self.numero_partidas} " \
               f"\nPuntuación media → {self.media_puntos} " \
               f"\nPartidas primero → {self.partidas_primero} " \
               f"\nPuesto medio → {self.puesto_medio}"



