# -*- coding: utf-8 -*-

import sys


def leer_entero(*args):
    """
    Función para leer un entero por teclado, controlando si se introduce algo que no es un entero.

    :param args:
    :return:
    """
    while True:
        try:
            for i in args:
                print(i, end="")
            return int(input())
        except ValueError:
            print("Dato erroneo, debe ser un número entero.", file=sys.stderr)


def leer_decimal(*args):
    """
    Función para leer un decimal por teclado, controlando si se introduce algo que no es un decimal (float).

    :param args:
    :return:
    """
    while True:
        try:
            for i in args:
                print(i, end="")
            return float(input())
        except ValueError:
            print("Dato erróneo, debe ser un número decimal.", file=sys.stderr)
