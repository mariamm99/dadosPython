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

    """
    @staticmethod
    def risco():

    @staticmethod
    def trece():

    @staticmethod
    def escalera_mayor():
    
    @staticmethod
    def escalera_menor():
    
    @staticmethod
    def escalera_par():
    
    @staticmethod
    def impar():
    
    @staticmethod
    def trio():

    @staticmethod
    def numero():
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
