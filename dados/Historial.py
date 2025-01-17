# -*- coding: utf-8 -*-

import re
import dados.Jugador as j


class Historial:
    """
    Historial es una clase para leer los ficheros de exportación de los
    jugadores que pueden crearse durante la partida.
    Muestra la Fecha de la partida, las puntuaciones, el número de
    jugadores que había y la posición del jugador en cuestión.
    """
    def __init__(self, player):
        self.nombre_jugador = player.nombre
        file = self.abrir_fichero()
        self.archivo = file
        lineas = self.cuenta_lineas()
        self.numero_partidas = lineas
        self.media_pnts = 0
        self.partidas_primero = 0
        self.puesto_medio = 0

    def nombre_jugador(self):
        """
        Devuelve el nombre del jugador
        :return: nombre del jugador
        """
        return self.nombre_jugador

    @property
    def numero_partidas(self):
        """
        Devuelve el número de partidas
        :return: nombre de partidas
        """
        return self.__numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, value):
        """
        Define el número de partidas
        :param value:
        """
        self.__numero_partidas = value

    @property
    def media_puntos(self):
        """
        Devuelve la media de puntos
        :return: media de puntos
        """
        puntos = 0
        prog = re.compile('Total:\s[0-9]{1,5}')
        texto_ = self.texto()
        lista_coincidencias = re.findall(prog, texto_)

        for coincidencia in lista_coincidencias:
            puntos += int(coincidencia[7:])

            puntos_f = puntos / self.numero_partidas
        return puntos_f

    @media_puntos.setter
    def media_puntos(self, value):
        """
        Define la media de puntos
        :param value:
        """
        self.media_pnts = value

    @property
    def partidas_primero(self):
        """
        Devuelve el número de partidas en las que el jugador ha quedado primero
        :return: partidas en las que el jugador va primero
        """
        prog = re.compile('Puesto:\s1')
        texto_ = self.texto()
        lista_coincidencias = re.findall(prog, texto_)

        for coincidencia in lista_coincidencias:
            self.__partidas_primero += 1

        return self.__partidas_primero

    @partidas_primero.setter
    def partidas_primero(self, value):
        """
        Define el número de partidas en las que el jugador ha quedado primero
        :param value:
        """
        self.__partidas_primero = value

    @property
    def puesto_medio(self):
        """
        Devuelve el puesto medio del jugador
        :return: posición media del jugador
        """
        posicion = 0
        prog = re.compile('Puesto:\s[0-9]{1,5}')
        texto_ = self.texto()
        lista_coincidencias = re.findall(prog, texto_)

        for coincidencia in lista_coincidencias:
            posicion += int(coincidencia[8:])

        posicion_f = posicion/self.numero_partidas

        return posicion_f

    @puesto_medio.setter
    def puesto_medio(self, value):
        """
        Define el puesto medio del jugador
        :param value:
        :return:
        """
        self.__puesto_medio = value

    def cuenta_lineas(self):
        """
        Cuenta todas las líneas del fichero, como cada línea es una partida, podemos considerar que
        hay tantas partidas como líneas.
        """
        contador = 0
        for line in self.archivo:
            contador += 1
        return contador

    def abrir_fichero(self):
        """
        Abre el fichero con la información del jugador
        """
        try:
            return open(f"risco_{self.nombre_jugador}.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            print("No se ha encontrado el archivo con tu historial.")

    def texto(self):
        """
        Lee el texto del fichero
        :return: texto del fichero
        """
        try:
            abrir_archivo = open(f"risco_{self.nombre_jugador}.txt", "r", encoding="utf-8")
            texto_leido = abrir_archivo.read()
            return texto_leido
        except FileNotFoundError:
            print("No se ha encontrado el archivo con tu historial.")

    def __str__(self):
        return f"\nHistorial de {self.nombre_jugador} " \
               f"\nPartidas hechas → {self.numero_partidas} " \
               f"\nPuntuación media → {self.media_puntos} " \
               f"\nPartidas primero → {self.partidas_primero} " \
               f"\nPuesto medio → {self.puesto_medio}"
