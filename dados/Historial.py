# -*- coding: utf-8 -*-

import re
import dados.Jugador as j


class Historial:
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
        return self.nombre_jugador

    @property
    def numero_partidas(self):
        return self.__numero_partidas

    @numero_partidas.setter
    def numero_partidas(self, value):
        self.__numero_partidas = value

    @property
    def media_puntos(self):
        veces = 0
        return 2

    @media_puntos.setter
    def media_puntos(self, value):
        self.media_pnts = value

    @property
    def partidas_primero(self):
        return self.__partidas_primero
        # No sé que funcionalidad tenía, lo comento temporalmente (Rafa)
        # texto = self.abrir_fichero()
        # return 0

    @partidas_primero.setter
    def partidas_primero(self, value):
        self.__partidas_primero = value

    @property
    def puesto_medio(self):
        prog = re.compile('Puesto:\s+(.*?)\n')
        texto_ = self.texto()
        result = prog.match(texto_)
        # m = prog.search(texto_)
        # print(m)
        #final=result.end()
        #print(final)

        #for i in range(final):
            # self.puesto_medio += int(result.group())
        #    print(result.group(i))

        while re.search(prog, texto_):
            print("aaaaaaaaaa")
            self.puesto_medio += int(result.group(1))
            print(self.puesto_medio)

        return 1

    @puesto_medio.setter
    def puesto_medio(self, value):
        self.__puesto_medio = value

    def cuenta_lineas(self):
        contador = 0
        for line in self.archivo:
            contador += 1
        return contador

    def abrir_fichero(self):
        try:
            return open(f"risco_{self.nombre_jugador}.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            print("No se ha encontrado el archivo con tu historial.")

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
