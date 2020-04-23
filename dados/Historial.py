# -*- coding: utf-8 -*-


import sys

class Historial:
    def __init__(self, player):
        self.nombre_jugador = player.get_nombre()
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
        self.archivo=value

    @property
    def numero_partidas(self):
        return self.numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, value):
        self.numero_partidas=value

    @property
    def media_puntos(self):
        veces = 0
        texto=texto()

    @media_puntos.setter
    def media_puntos(self, value):
        self.media_puntos= value

    @property
    def partidas_primero(self):
        texto=texto()

    @partidas_primero.setter
    def partidas_primero(self, value):
        self.partidas_primero=value

    @property
    def puesto_medio(self):


    @puesto_medio.setter
    def puesto_medio(self, value):
        self.puesto_medio=value

    def abrir_fichero(self):

    def cuenta_lineas(self):
        n_partidas=0

    def leer_fichero(self):

    def texto(self):

    def __str__(self):



