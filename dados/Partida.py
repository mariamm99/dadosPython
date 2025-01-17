# -*- coding: utf-8 -*-
import dados.Jugador as j
import dados.Dados as d


class Partida:
    """
    Partida es la clase en la que se encuentran los métodos para todos los "juegos"
    que se pueden jugar en el Risco, como el trío, la escalera mayor, etc.

    Se tienen en cuenta la ronda y el número de jugadores que hay en la partida.

    También contiene todos los jugadores de la clase Jugador que están jugando la
    partida.

    Además, desde aqui se pueden crear nuevos jugadores, tirar unos nuevos dados,
    generar el tablero con todas las puntuaciones o calcular cual es la posición
    en la que está el jugador.
    """
    def __init__(self, nj):
        self.n_jugadores = nj
        self.ronda = 1
        self.jugadores = []  # Equivale a ArrayList jugadores en Java

    @property
    def n_jugadores(self):
        return self.__n_jugadores

    @n_jugadores.setter
    def n_jugadores(self, value):
        self.__n_jugadores = value

    @property
    def ronda(self):
        return self.__ronda

    @ronda.setter
    def ronda(self, value):
        self.__ronda = value

    def __str__(self):
        return "\n Partida ronda=", self.ronda, ", nJugadores=", self.n_jugadores

    def crear_jugadores(self, nj, nombre):
        """
        Método para crear jugadores para la partida
        :param nj:
        :param nombre:
        """
        self.jugadores.append(j.Jugador(nj, nombre))

    @staticmethod
    def tirar_dados(player):
        """
        Método para que el jugador tire sus dados
        :param player:
        :return: dados del jugador
        """
        player.dados_jugador = d.Dados()
        return player.dados_jugador

    def muestra_tablero(self):
        """
        Método que imprime por pantalla el tablero con las puntuaciones de cada jugador
        """
        juegos = "\t", "Risco", "Trece", "E.Mayor", "E.Menor", "E.Par", "E.Impar", "Trio", "Seis", "Cinco", "Cuatro", "Tres", "Dos ", "As  ", "Total"

        for i in range(len(juegos)):
            print(juegos[i], end="\t")

        for i in range(self.n_jugadores):
            for k in range(0, 15):

                if k == 0:
                    print("\n", self.jugadores[self.jugadores.index(j.Jugador(i))].nombre, "\t", end="\t")

                else:
                    if self.jugadores[self.jugadores.index(j.Jugador(i))].ptos[k] is not None:
                        print(self.jugadores[self.jugadores.index(j.Jugador(i))].ptos[k], "\t", end="\t")
                    else:
                        print("\t", end="\t")

    @staticmethod
    def risco(player):
        """
        Método de comprobación de juego: Risco
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        if not casilla_vacia(player, 1):
            return 50
        if (player.dados_jugador.get_d1 == player.dados_jugador.get_d2 or player.dados_jugador.get_d1 == \
                player.dados_jugador.get_d3 or player.dados_jugador.get_d2 == player.dados_jugador.get_d3) and \
                player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(1, 50)
            player.ptos.insert(14, player.total_ptos(1))
            return 1
        else:
            player.ptos.insert(1, 0)
            player.ptos.insert(14, player.total_ptos(1))
            return 0

    @staticmethod
    def trece(player):
        """
        Método de comprobación de juego: Trece
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        if not casilla_vacia(player, 2):
            return 50
        if player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(2, 26)
            player.ptos.insert(14, player.total_ptos(2))
            return 1
        else:
            player.ptos.insert(2, 0)
            player.ptos.insert(14, player.total_ptos(2))
            return 0

    @staticmethod
    def escalera_mayor(player):
        """
        Método de comprobación de juego: Escalera mayor
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not casilla_vacia(player, 3):
            return 50

        for i in range(4, 7):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(3, 0)
                player.ptos.insert(14, player.total_ptos(3))
                return 0

            if valord1 and valord2 and valord3:
                player.ptos.insert(3, 20)
                player.ptos.insert(14, player.total_ptos(3))
                return 1

    @staticmethod
    def escalera_menor(player):
        """
        Método de comprobación de juego: Escalera menor
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not casilla_vacia(player, 4):
            return 50

        for i in range(1, 4):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(4, 0)
                player.ptos.insert(14, player.total_ptos(4))
                return 0

            if valord1 and valord2 and valord3:
                player.ptos.insert(4, 20)
                player.ptos.insert(14, player.total_ptos(4))
                return 1

    @staticmethod
    def escalera_par(player):
        """
        Método de comprobación de juego: Escalera par
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not casilla_vacia(player, 5):
            return 50

        for i in range(2, 7, 2):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(5, 0)
                player.ptos.insert(14, player.total_ptos(5))
                return 0

            if valord1 and valord2 and valord3:
                player.ptos.insert(5, 20)
                player.ptos.insert(14, player.total_ptos(5))
                return 1

    @staticmethod
    def escalera_impar(player):
        """
        Método de comprobación de juego: Escalera impar
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not casilla_vacia(player, 6):
            return 50

        for i in range(1, 6, 2):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(6, 0)
                player.ptos.insert(14, player.total_ptos(6))
                return 0

            if valord1 and valord2 and valord3:
                player.ptos.insert(6, 20)
                player.ptos.insert(14, player.total_ptos(6))
                return 1

    @staticmethod
    def trio(player):
        """
        Método de comprobación de juego: Trío
        :param player:
        :return: 1 si acierta, 0 si no y 50 si la casilla está vacía
        """
        if not casilla_vacia(player, 7):
            return 50
        if player.dados_jugador.get_d1 == player.dados_jugador.get_d2 and player.dados_jugador.get_d1 == player.dados_jugador.get_d3:
            player.ptos.insert(7, 25)
            player.ptos.insert(14, player.total_ptos(7))
            return 1

        else:
            player.ptos.insert(7, 0)
            player.ptos.insert(14, player.total_ptos(7))
            return 0

    @staticmethod
    def numero(player, n):
        """
        Método de comprobación de juego: Seis, cinco, cuatro, tres, dos y as
        :param player:
        :param n:
        :return: Puntos obtenidos o 50 si la casilla está vacía
        """
        puntos = 0
        if player.dados_jugador.get_d1 == n:
            puntos += n

        if player.dados_jugador.get_d2 == n:
            puntos += n

        if player.dados_jugador.get_d3 == n:
            puntos += n

        casilla = 0

        if n == 6:
            casilla = 8
        elif n == 5:
            casilla = 9
        elif n == 4:
            casilla = 10
        elif n == 3:
            casilla = 11
        elif n == 2:
            casilla = 12
        elif n == 1:
            casilla = 13

        if not casilla_vacia(player, casilla):
            return 50
        player.ptos.insert(casilla, puntos)
        player.ptos.insert(14, player.total_ptos(casilla))
        return puntos

    def posicion(self, player):
        """
        Método para calcular la posición en la que va el jugador que se le pase como parámetro.
        Compara la puntuación del jugador con la del resto, y si es mayor, incrementa la posición
        en uno.
        :param player:
        :return: posición del jugador
        """
        pos = 1
        puntos = player.ptos[14]  # Se coloca el número de la posición del total

        for i in range(0, self.n_jugadores):
            if self.jugadores[self.jugadores.index(j.Jugador(i))].ptos[14] is not None:
                if self.jugadores[self.jugadores.index(j.Jugador(i))].ptos[14] > puntos:
                    pos += 1

        return pos


def casilla_vacia(player, casilla):
    """
    Método para comprobar si una casilla del tablero esta vacía.
    :param player:
    :param casilla:
    :return: boolean, True si la casilla está vacía, False si no está vacía
    """
    if player.ptos[casilla] is None:
        return True
    else:
        return False
