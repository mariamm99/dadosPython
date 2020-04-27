# -*- coding: utf-8 -*-
import dados.Dados as d
import sys
import time


class Jugador:
    """
    Método Jugador. Crea el jugador con los datos de cada jugador: nombre, numero de jugador,
    arraylist con las puntuaciones y el resultado de los dados del jugador.

    Además de la información del jugador, en esta clase creamos el método encargado de exportar los datos
    del jugador a un archivo txt que se llamara risco_<nombre del jugador>.txt. Esta función nos permitirá
    guardar los datos de la partida( su puntuación, puesto en el que ha quedado, contra cuantos jugadores
    jugaba, etc)
    """

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
        self.total_puntos = 0  # Variable para la puntuación total del jugador
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
    def total_puntos(self):
        """
        puntos totales del jugador
        :return: total_puntos
        """
        return self.__total_puntos

    @total_puntos.setter
    def total_puntos(self, value):
        """
        Da valor a los puntos totales
        :param value:
        """
        self.__total_puntos = value

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
            self.total_puntos += self.ptos[i]
            hay_ptos = True

        if hay_ptos:
            return self.total_puntos
        else:
            return 0

    def crea_archivo(self):
        """
        Método para crear archivos para la exportación de datos.

        :return:
        """
        nombre_fichero = f"risco_{self.nombre}.txt"
        try:
            return open(nombre_fichero, "a")
        except PermissionError or FileNotFoundError:
            print("ERROR al escribir en " + nombre_fichero, file=sys.stderr)

    def guarda_datos(self, n_jugadores, pos):
        """
        Método para escribir en un archivo los datos actuales del jugador.

        Estructura:
        Fecha: 21/04/2020 ; Risco: 50 ; Trece: 20 ; E.Mayor: 10 ; ... Total: 817 ; Número jugadores: 2 ; Puesto: 1

        :return:
        """
        file = self.crea_archivo()

        # Fecha
        date = time.strftime("%d/%m/%Y")  # Arreglar
        file.write(f"Fecha: {date} ; ")

        # Puntuación
        juegos = ["Risco: ", "Trece:  ", "E.Mayor: ", "E.Menor: ", "E.Par: ", "E.Impar: ", "Trio: ", "Seis: ",
                  "Cinco: ", "Cuatro: ", "Tres: ", "Dos: ", "As: ", "Total: "]
        for i in range(0, len(juegos)):
            if self.ptos[i+1] is not None:
                file.write(f"{juegos[i]}{self.ptos[i+1]} ; ")
            else:
                file.write(f"{juegos[i]}\t ; ")

        # Número de jugadores
        file.write(f"Número jugadores: {n_jugadores} ; ")  # 0 Cambiar por número real, que se pasará como param

        # Puesto en la partida
        file.write(f"Puesto: {pos}")  # 0 Cambiar por posición real, que se pasará como param

        # Final
        file.write("\n")
        file.close()
        print("Datos exportados.")

    # Métodos sobrecargados
    def __eq__(self, other):
        if not isinstance(other, Jugador):
            raise TypeError
        return self.nj == other.nj

    def __str__(self):
        return f"Jugador: {self.nombre}\nDados Jugador:\n{self.dados_jugador}"
