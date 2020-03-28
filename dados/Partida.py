# -*- coding: utf-8 -*-
import dados.Jugador as j
import dados.Dados as d


class Partida:
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
        return "\n Partida ronda=", self.ronda ,", nJugadores=", self.n_jugadores

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
        player.dados_jugador = d.Dados()
        return player.dados_jugador

    def muestra_tablero(self):
        juegos = ["\tRisco", "Trece", "E.Mayor", "E.Menor", "E.Par", "E.Impar", "Trio", "Seis", "Cinco", "Cuatro",
                  "Tres", "Dos", "As", "Total"]

        for i in juegos:
            print(juegos[i] + "\t")

        for i in self.n_jugadores:
            for j in range(0, 14):
                if j == 0:
                    print("\n", j)
                else:
                    if False:  # Temporal para que no falle, cambiar, IMPORTANTE.
                        print("")  # El fallo que da aqui es porque al ser False nunca lo va a ejecutar.
                    else:
                        print("\t")

    @staticmethod
    def casilla_vacia(player, casilla):
        if player[casilla]:
            return True
        else:
            return False

    @staticmethod
    def risco(player):
        if player.dados_jugador.get_d1 == player.dados_jugador.get_d2 or player.dados_jugador.get_d1 == \
                player.dados_jugador.get_d3 or player.dados_jugador.get_d2 == player.dados_jugador.get_d3 and \
                player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(0, 50)
            player.ptos.insert(13, player.total_ptos(0))
            return "Casilla Risco completa, 50 puntos"
        else:
            player.ptos.insert(0, 0)
            player.ptos.insert(13, player.total_ptos(0))
            return "Esta combinación de números no es un risco 0 puntos"

    @staticmethod
    def trece(player):
        if player.dados_jugador.get_d1 + player.dados_jugador.get_d2 + player.dados_jugador.get_d3 == 13:
            player.ptos.insert(1, 26)
            player.ptos.insert(13, player.total_ptos(1))

            return "Casilla trece completa, 26 puntos"
        else:
            player.ptos.insert(1, 0)
            player.ptos.insert(13, player.total_ptos(1))
            return "Esta combinación de números no es un trece, 0 puntos"

    @staticmethod
    def escalera_mayor(player):
        valord1 = False
        valord2 = False
        valord3 = False

        for i in range(4, 7):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(2, 0)
                player.ptos.insert(13, player.total_ptos(2))
                return "Esta combinaciÃ³n de dados no es una Escalera Mayor"

            if valord1 and valord2 and valord3:
                player.ptos.insert(2, 20)
                player.ptos.insert(13, player.total_ptos(2))
                return "Esta combinación es una Escalera Mayor, 20 ptos"

    @staticmethod
    def escalera_menor(player):
        valord1 = False
        valord2 = False
        valord3 = False

        for i in range(1, 4):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(3, 0)
                player.ptos.insert(13, player.total_ptos(2))
                return "Esta combinación de dados no es una Escalera Menor"

            if valord1 and valord2 and valord3:
                player.ptos.insert(3, 20)
                player.ptos.insert(13, player.total_ptos(3))
                return "Esta combinación es una Escalera Menor, 20 ptos"

    @staticmethod
    def escalera_par(player):
        valord1 = False
        valord2 = False
        valord3 = False

        for i in range(2, 7, 2):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(4, 0)
                player.ptos.insert(13, player.total_ptos(4))
                return "Esta combinación de dados no es una Escalera Par"

            if valord1 and valord2 and valord3:
                player.ptos.insert(4, 20)
                player.ptos.insert(13, player.total_ptos(4))
                return "Esta combinación es una Escalera Par, 20 ptos"

    @staticmethod
    def escalera_impar(player):
        valord1 = False
        valord2 = False
        valord3 = False

        for i in range(1, 6, 2):
            if player.dados_jugador.get_d1 == i:
                valord1 = True
            elif player.dados_jugador.get_d2 == i:
                valord2 = True
            elif player.dados_jugador.get_d3 == i:
                valord3 = True

            else:
                player.ptos.insert(5, 0)
                player.ptos.insert(13, player.total_ptos(5))
                return "Esta combinación de dados no es una escalera impar"

            if valord1 and valord2 and valord3:
                player.ptos.insert(5, 20)
                player.ptos.insert(13, player.total_ptos(5))
                return "Esta combinación es una escalera impar, 20 ptos"

    @staticmethod
    def trio(player):
        if player.dados_jugador.get_d1 == player.dados_jugador.get_d2 or player.dados_jugador.get_d1() and \
                player.dados_jugador.get_d3:
            player.ptos.insert(6, 25)
            player.ptos.insert(13, player.total_ptos(6))
            return "Casilla Trío completada, 25 ptos"

        else:
            player.ptos.insert(6, 0)
            player.ptos.insert(13, player.total_ptos(6))
            return "Esta combinación de números no es un trío."

    @staticmethod
    def numero(player, n):
        puntos = 0
        if player.dados_jugador.get_d1 == n:
            puntos += n

        if player.dados_jugador.get_d1 == n:
            puntos += n

        if player.dados_jugador.get_d1 == n:
            puntos += n

        casilla = 0

        if n == 6:
            casilla = 7
        elif n == 5:
            casilla = 8
        elif n == 4:
            casilla = 9
        elif n == 3:
            casilla = 10
        elif n == 2:
            casilla = 11
        elif n == 1:
            casilla = 12

        player.ptos.insert(casilla, puntos)
        player.ptos.insert(13, player.total_ptos(casilla))
        return "Casilla" + n + "completada con " + n + " ptos"


"""
if __name__ == "__main__":
    # Todo lo que hay aqui es sólo para pruebas y habrá que borrarlo al acabar o antes.
    # Prueba de crear un jugador y ver su información
    partida = Partida(1)
    partida.crear_jugadores(1, "Rafa")
    # Mostrar nombre jugador 1
    jugador_a_buscar = j.Jugador(1)
    var = str(partida.jugadores[partida.jugadores.index(jugador_a_buscar)])
    print(var)
    print(partida.risco(jugador_a_buscar))
"""
