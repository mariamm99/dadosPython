# -*- coding: utf-8 -*-
import dados.Dados as d
import sys
from datetime import datetime


class Jugador:

    # Constructor
    def __init__(self, n_jugadores, nombre):
        self.nj = n_jugadores  # Número de jugadores
        self.nombre = nombre  # Nombre del jugador
        self.dados_jugador = d.Dados()  # Dados del jugador
        self.total_base = 0  # Variable para la puntuación total del jugador
        self.ptos = []
        for i in range(0, 13):
            self.ptos.append(None)  # Array de puntuaciones, en el momento de la creación vacío

    def total_ptos(self, i):
        """
        Método para calcular el total de puntos del jugador
        :param i:
        :return:
        """
        hay_ptos = False

        if self.ptos[i] is not None:
            self.total_base += self.ptos[i]
            hay_ptos = True

        if hay_ptos:
            return self.total_base
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
        return self.nombre() == other.nombre()

    def __str__(self):
        return f"Jugador [nombre={self.nombre}, dados_jugador={self.dados_jugador}]"
