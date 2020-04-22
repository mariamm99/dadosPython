# -*- coding: utf-8 -*-
import dados.Jugador as j
import dados.Dados as d


class Partida:
    def __init__(self, nj):
        """
        Consturctor de partida
        :param nj: numero de jugadores
        """
        self.n_jugadores = nj
        self.ronda = 1
        self.jugadores = []  # Equivale a ArrayList jugadores en Java

    @property
    def n_jugadores(self):
        """
        :return:  numero de jugadores
        """
        return self.__n_jugadores

    @n_jugadores.setter
    def n_jugadores(self, value):
        """
        :param value: indica el numero de jugadores
        """
        self.__n_jugadores = value

    @property
    def ronda(self):
        """
        :return: ronda de la partida
        """
        return self.__ronda

    @ronda.setter
    def ronda(self, value):
        """
        :param value: ronda de la partida
        """
        self.__ronda = value

    def __str__(self):
        return "\n Partida ronda=", self.ronda, ", nJugadores=", self.n_jugadores

    def crear_jugadores(self, nj, nombre):
        """
        Método para crear jugadores para la partida
        :param nj:
        :param nombre:
        :return:
        """
        self.jugadores.append(j.Jugador(nj, nombre))

    @staticmethod
    def tirar_dados(player):
        """
        Da valor a los dados del jugador
        :param player:
        :return: dados del jugador
        """
        player.dados_jugador = d.Dados()
        return player.dados_jugador

    def muestra_tablero(self):
        """
        muestra el tablero con las puntuaciones de cada jugador.
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

    def casilla_vacia(self, player, casilla):
        """
        comprueba si la casilla del jugador indicado esta vacia
        :param player:
        :param casilla:
        :return: True o False si esta vacia o no.
        """
        if player[casilla]:
            return True
        else:
            return False

    @staticmethod
    def risco(player):
        """
        Risco: cuando dos dados son inguales y junto con el tercero suman 13
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        if player.casilla_vacia(1) is False:
            return "casilla ocupada"

        if player.dados_jugador.get_d1 == player.dados_jugador.get_d2 or player.dados_jugador.get_d1 == \
                player.dados_jugador.get_d3 or player.dados_jugador.get_d2 == player.dados_jugador.get_d3 and \
                player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(1, 50)
            player.ptos.insert(14, player.total_ptos(1))
            return "Casilla Risco completa, 50 puntos"
        else:
            player.ptos.insert(1, 0)
            player.ptos.insert(14, player.total_ptos(1))
            return "Esta combinación de números no es un risco 0 puntos"

    @staticmethod
    def trece(player):
        """
        Trece: si la suma de los 3 dados da 13
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        if not casilla_vacia(player, 2):
            return "casilla ocupada"

        if player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(2, 26)
            player.ptos.insert(14, player.total_ptos(2))

            return "Casilla trece completa, 26 puntos"
        else:
            player.ptos.insert(2, 0)
            player.ptos.insert(14, player.total_ptos(2))
            return "Esta combinación de números no es un trece, 0 puntos"

    @staticmethod
    def escalera_mayor(player):
        """
        Escalera mayor: Si los numeros de los dados son 4, 5 y 6
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not player.casilla_vacia(3):
            return "casilla ocupada"

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
                return "Esta combinaciÃ³n de dados no es una Escalera Mayor"

            if valord1 and valord2 and valord3:
                player.ptos.insert(3, 20)
                player.ptos.insert(14, player.total_ptos(3))
                return "Esta combinación es una Escalera Mayor, 20 ptos"

    @staticmethod
    def escalera_menor(player):
        """
        Escalera Menor: si el valor de los dados son 1, 2 y 3
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not player.casilla_vacia(4):
            return "casilla ocupada"

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
                return "Esta combinación de dados no es una Escalera Menor"

            if valord1 and valord2 and valord3:
                player.ptos.insert(4, 20)
                player.ptos.insert(14, player.total_ptos(4))
                return "Esta combinación es una Escalera Menor, 20 ptos"

    @staticmethod
    def escalera_par(player):
        """
        Escalera par: los dados tienen valor 2, 4 y 6
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        valord1 = False
        valord2 = False
        valord3 = False
        if not player.casilla_vacia(5):
            return "casilla ocupada"

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
                return "Esta combinación de dados no es una Escalera Par"

            if valord1 and valord2 and valord3:
                player.ptos.insert(5, 20)
                player.ptos.insert(14, player.total_ptos(5))
                return "Esta combinación es una Escalera Par, 20 ptos"

    @staticmethod
    def escalera_impar(player):
        """
        Escalera Impar: los dados tienen valor 1, 3 y 5
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        valord1 = False
        valord2 = False
        valord3 = False

        if not player.casilla_vacia(6):
            return "casilla ocupada"

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
                return "Esta combinación de dados no es una escalera impar"

            if valord1 and valord2 and valord3:
                player.ptos.insert(6, 20)
                player.ptos.insert(14, player.total_ptos(6))
                return "Esta combinación es una escalera impar, 20 ptos"

    @staticmethod
    def trio(player):
        """
        trio: si los 3 dados son iguales
        :param player:
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
        """
        if not player.casilla_vacia(7):
            return "casilla ocupada"

        if player.dados_jugador.get_d1 == player.dados_jugador.get_d2 and player.dados_jugador.get_d1() == player.dados_jugador.get_d3:
            player.ptos.insert(7, 25)
            player.ptos.insert(14, player.total_ptos(7))
            return "Casilla Trío completada, 25 ptos"

        else:
            player.ptos.insert(7, 0)
            player.ptos.insert(14, player.total_ptos(7))
            return "Esta combinación de números no es un trío."

    @staticmethod
    def numero(player, n):
        """
        Número: según el numero indicando la puntuación sera el numero elegido por las veces que aparece en los dados
        Ej: si los dados son 3, 3, 1 si eliges tres obrendras 6 puntos.
        :param player:
        :param n: numero elegido en el menú (Ej: seises, cuatros, ases..)
        :return: String indicando si la casilla esta ocupada o si se ha completado con que puntuación.
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

        if not player.casilla_vacia(1):
            return "casilla ocupada"
        else:
            player.ptos.insert(casilla, puntos)
            player.ptos.insert(14, player.total_ptos(casilla))
            return "Casilla " + str(n) + " completada con " + str(n) + " ptos"
