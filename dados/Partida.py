# -*- coding: utf-8 -*-
import dados.Jugador as j
import dados.Dados as d

class Partida:
    def __init__(self, n_jugadores):
        self.n_jugadores = n_jugadores
        self.ronda = 1
        self.jugador = []
    
    @property
    def get_n_jugadores(self):
        return self.n_jugadores

    @n_jugadores.setter
    def set_n_jugadores(self , n_jugadores):
        self.n_jugadores = n_jugadores

    @property
    def get_ronda(self):
        self.ronda

    @ronda.setter
    def set_ronda(self , ronda):
        self.ronda = ronda


    def crear_jugadores(self , nj , nombre):
        self.jugador.append(j.Jugador(nj,nombre))

    @staticmethod
    def tirar_dados(player):
        player.dados_jugador = d.Dados()
        return player.dados_jugador

    def muestra_tablero(self):
        juegos = ["\tRisco","Trece","E.Mayor","E.Menor","E.Par","E.Impar","Trio","Seis","Cinco","Cuatro","Tres","Dos","As","Total"]

        for i in range (juegos):
            print(juegos[i],"\t")

        for i in range (self.get_n_jugadores):
            for j in range (15):
                if (j == 0):
                    print("\n" , j)
                else:
                    if ():
                        print()
                    else:
                        print("\t")

    @staticmethod
    def casilla_vacia(player , casilla):
        if (player[casilla]) :
            return True
        else :
            return False
    
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

    