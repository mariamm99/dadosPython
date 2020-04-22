# -*- coding: utf-8 -*-

import dados.Dados as d
import sys

class Historial:
    def __init__(self, player):
        self.nombre_jugador = player.get_nombre()
        self.archivo = abrir_fichero()
        self.numero_partidas = cuenta_lineas()
        self.media_puntos = 0
        self.partidas_primero = 0
        self.puesto_medio = 0;

    def nombre_jugador(self):
        return self.nombre_jugador

 #no se como hacer lo del buffer
    def get_archivo(self):
        return self.archivo

#buffer igual
    def set_archivo(self):

    def get_numero_partidas(self):
        return self.numero_partidas

    def set_numero_partidas(self, numero_partidas):
        self.numero_partidas=numero_partidas

    def get_media_puntos(self):
        veces = 0
        texto=texto()

    def set_media_puntos(self, media_puntos):
        self.media_puntos=media_puntos

    def get_partidas_primero(self):
        texto=texto()

    def set_partidas_primero(self):

    def get_puesto_medio(self):

    def set_puesto_medio(self):

    def abrir_fichero(self):

    def cuenta_lineas(self):
        n_partidas=0

    def leer_fichero(self):

    def texto(self):

    def __str__(self):



