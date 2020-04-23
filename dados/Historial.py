# -*- coding: utf-8 -*-

import re

class Historial:
    def __init__(self, player):
        self.nombre_jugador = player.nombre
        self.archivo = abrir_fichero()
        self.numero_partidas = cuenta_lineas()
        self.media_puntos = 0
        self.partidas_primero = 0
        self.puesto_medio = 0

    def nombre_jugador(self):
        return self.nombre_jugador

    #no se como hacer lo del buffer
    @property
    def archivo(self):
        return self.archivo

    #buffer igual
    @archivo.setter
    def archivo(self, value):
        self.archivo = value

    @property
    def numero_partidas(self):
        return self.numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, value):
        self.numero_partidas = value

    @property
    def media_puntos(self):
        veces = 0
        texto = self.texto()

    @media_puntos.setter
    def media_puntos(self, value):
        self.media_puntos = value

    @property
    def partidas_primero(self):
        texto = self.texto()

    @partidas_primero.setter
    def partidas_primero(self, value):
        self.partidas_primero = value

    @property
    def puesto_medio(self):
        veces = 0
        texto = self.texto()
        m = re.search("Puesto:\s+(.*?)\n", texto)

        while linea is not None:
            self.puesto_medio += int(m.group(1))
            linea = self.archivo.readlines()
            veces += 1
        return self.puesto_medio/veces

    @puesto_medio.setter
    def puesto_medio(self, value):
        self.puesto_medio = value

    def cuenta_lineas(self):
        return len(self.archivo.readlines())

    def texto(self):
        try:
            texto = open(self.archivo, "r", encoding="utf-8")
            texto_leido = texto.read()
            return texto_leido
        except FileNotFoundError:
            print("no se ha encontrado el archivo")
            exit(3)

    def __str__(self):
        # Comprobar que devuelve los valores bien una vez esté la clase acabada
        return f"\nHistorial de {self.nombre_jugador()} " \
               f"\nPartidas hechas → {self.numero_partidas} " \
               f"\nPuntuación media → {self.media_puntos} " \
               f"\nPartidas primero → {self.partidas_primero} " \
               f"\nPuesto medio → {self.puesto_medio}"



