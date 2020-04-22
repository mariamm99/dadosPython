# -*- coding: utf-8 -*-
import dados.Dados as d
import sys
from datetime import datetime


class Jugador:

    def __init__(self, *args):
        """
        Constructor de Jugador
        :param args: puede variar el número de argumentos pasados al constructor
        """
        if len(args) == 1:
            self.nj = args[0]  # Número del jugador
        if len(args) == 2:
            self.nj = args[0]  # Número del jugador
            self.nombre = args[1]  # Nombre del jugador
        self.dados_jugador = d.Dados()  # Dados del jugador
        self.total_ptos = 0  # Variable para la puntuación total del jugador
        self.ptos = []
        for i in range(15):
            self.ptos.append(None)  # Array de puntuaciones, en el momento de la creación vacío

    # Getters & Setters
    @property
    def nj(self):
        """
        :return:  numero de jugadores
        """
        return self.__nj

    @nj.setter
    def nj(self, value):
        """
        Set de numero de jugador
        :param value:
        """
        self.__nj = value

    @property
    def nombre(self):
        """
        :return: nombre del jugador
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        """
        Set da valor al nombre del jugador
        :param value:
        """
        self.__nombre = value

    @property
    def dados_jugador(self):
        """
        :return: Dados del jugador
        """
        return self.__dados_jugador

    @dados_jugador.setter
    def dados_jugador(self, value):
        """
        Da valor a los dados del jugador
        :param value:
        """
        self.__dados_jugador = value

    @property
    def total_ptos(self):
        """
        puntos totales del jugador
        :return: total_ptos
        """
        return self.__total_ptos

    @total_ptos.setter
    def total_ptos(self, value):
        """
        Da valor a los puntos totales
        :param value:
        """
        self.__total_ptos = value

    @property
    def ptos(self):
        return self.__ptos

    @ptos.setter
    def ptos(self, value):
        self.__ptos = value

    # Métodos
    def total_ptos(self, i):
        """
        Método para calcular el total de puntos del jugador
        :param i:
        :return:
        """
        hay_ptos = False

        if self.ptos[i] is not None:
            self.total_ptos += self.ptos[i]
            hay_ptos = True

        if hay_ptos:
            return self.total_ptos
        else:
            return 0

    def crea_archivo(self):
        """
        Método para crear archivos para la exportación de datos.

        :return:
        """
        nombre_fichero = f"{self.nombre}.txt"
        try:
            return open(nombre_fichero, "w")
        except PermissionError or FileNotFoundError:
            print("ERROR al escribir en " + nombre_fichero, file=sys.stderr)

    def guarda_datos(self):
        """
        Método para escribir en un archivo los datos actuales del jugador.

        :return:
        """
        file = self.crea_archivo()

        # Nombre
        file.write(f"Nombre de jugador: {self.nombre}")
        file.newlines()
        file.write("---------------------")
        file.newlines()

        # Dados
        file.write(f"Dados actuales de {self.nombre}")
        file.newlines()
        file.write(self.dados_jugador)  # IMPORTANTE: Debe estar sobrecargado __str__ en Dados, quitar cuando esté
        file.newlines()

        # Puntuación
        file.write(f"\nPuntuación actual de {self.nombre}")
        file.newlines()
        juegos = ["\nRisco → ", "Trece → ", "E.Mayor → ", "E.Menor → ", "E.Par → ", "E.Impar → ", "Trio → ", "Seis → ",
                  "Cinco → ", "Cuatro → ", "Tres → ", "Dos → ", "As → ", "Total → "]
        for i in juegos:
            if self.ptos[i] is not None:
                file.write(f"{juegos[i]}{self.ptos[i]}")
            else:
                file.write(f"{juegos[i]}\t")
            file.newlines()

        # Final
        file.write(f"Datos exportados a {datetime.now()}")
        file.close()
        print("Datos exportados.")

    # Métodos sobrecargados
    def __eq__(self, other):
        if not isinstance(other, Jugador):
            raise TypeError
        return self.nj == other.nj

    def __str__(self):
        return f"Jugador: {self.nombre}\nDados Jugador:\n{self.dados_jugador}"
