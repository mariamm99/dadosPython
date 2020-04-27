# -*- coding: utf-8 -*-
import random


class Dados:
    """
    Método dados. Encargado de generar los dados de la partida de forma aleatoria de 1 al 6.
    Muestra el resultado de los 3 dados.
    Además, permite cambiar el resultado de los dados que quiera el jugador.
    """

    def __init__(self):
        """
        Constructor de dados, da valores aleatorios a los 3 dados.
        """
        self.set_d1()
        self.set_d2()
        self.set_d3()

    @property
    def get_d1(self):
        """
        get de dado 1, devuelve el valor del dado 1.
        :return: d1
        """
        return self.d1

    def set_d1(self):
        """
        set d1, da valor aleatorio a dado 1
        """
        self.d1 = int(random.randint(1, 6))

    @property
    def get_d2(self):
        return self.d2

    def set_d2(self):
        """
        set d2, da valor aleatorio a dado 1
        """
        self.d2 = int(random.randint(1, 6))

    @property
    def get_d3(self):

        return self.d3

    def set_d3(self):
        """
        set d1, da valor aleatorio a dado 1
        """
        self.d3 = int(random.randint(1, 6))

    def __str__(self):
        return "Dado 1: " + str(self.d1) + "\nDado 2: " + str(self.d2) + "\nDado 3: " + str(self.d3)

    def cambiar_dados(self, ndados_cambiar):
        """
        Cambia el valor de los dados indicados
        :param ndados_cambiar:
        :return: __str__ de dados
        """

        """
        Si se indica que quieres cambiar mas de dos dados te cambia los 3 dados.
        """
        if ndados_cambiar > 2:
            if ndados_cambiar > 3:
                print("Solo puedes cambiar 3 dados, se cambiaran los 3")
            self.set_d1()
            self.set_d2()
            self.set_d3()

            return self.__str__()

        cambiod1 = True
        cambiod2 = True
        cambiod3 = True

        """
        Bucle para cambiar el valor de los dados.
        Evita que cambien varias veces el valor del mismo dado
        """
        for i in range(0, ndados_cambiar):
            i += 1
            dado = int(input("Indique que dado quiere cambiar, 1 , 2 o 3"))
            if dado == 1 and cambiod1:
                self.set_d1()
                cambiod1 = False
            elif dado == 2 and cambiod2:
                self.set_d2()
                cambiod2 = False
            elif dado == 3 and cambiod3:
                self.set_d3()
                cambiod3 = False

            elif cambiod3 is False or cambiod2 is False or cambiod1 is False:
                print("Dado " + str(dado) + " ya ha sido cambiado introduzca otro")
                i -= 1

            else:
                print("Dado " + str(dado) + " no existe introduzca otro")
                i -= 1
        return self.__str__()
