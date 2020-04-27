# -*- coding: utf-8 -*-
import utiles.Teclado as t


class Menu:
    """
    Clase Menu. gestiona las opciones del menú.
    """
    # Constructor Menu
    def __init__(self, titulo, opciones):
        self.titulo = titulo
        self.opciones = opciones
        self.n_opciones = len(opciones)

    def gestionar(self):
        """
        Método encargado de gestionar el menú, muestra y recoge la opción indicada por el usuario
        :return:
        """
        self.mostrar()
        return self.recoger_opcion()

    def mostrar(self):
        """
        Método para mostrar todas las opciones
        :return:
        """
        print(f"\n**{self.titulo}")
        for i in range(self.n_opciones):
            print(f"({i + 1}) {self.opciones[i]}")

    def recoger_opcion(self):
        """
        Método para recoger la opción

        :return:
        """
        opcion = t.leer_entero("Indique la opción: ")
        while opcion > self.n_opciones or opcion < 1:
            print("Esa opción no es válida...")
            opcion = t.leer_entero("Indique la opción: ")
        return opcion
