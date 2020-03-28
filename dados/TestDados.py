# -*- coding: utf-8 -*-
import utiles.Menu as m
import utiles.Teclado as t
import dados.Partida as p
from dados import Partida
import dados.Jugador as j


class TestPartida:
    opciones = "Risco", "Trece", "Escalera Mayor", "Escalera Menor ", "Escalera par", "Escalera impar", "Trio", "Seis", "Cinco", "Cuatro", "Tres", "Dos", "Ases"
    menu = m.Menu("Indique la opción que quiere realizar:", opciones)


if __name__ == "__main__":
    nJugadores = t.leer_entero("Indica cuantos jugadores sois: ")

    partida = p.Partida(nJugadores)

    for i in range(0, nJugadores):
        nombreTmp = input("Introduce el nombre del jugador")
        p.Partida.crear_jugadores(i, nombreTmp)
        i += 1

    for i in range(1, 14):
        for k in range(1, nJugadores + 1):

            player = j.Jugador.get(p.Partida.jugadores.indexOf(j.Jugador(k)))

            print("\n Turno " + i + "del jugador" + (p.Partida.jugadores.indexOf(j.Jugador(k))).getNombre())

            print("\nEn esta tirada obtienes:\n"
                  + p.Partida.tirarDados(p.Partida.jugadores.get(p.Partida.jugadores.indexOf(j.Jugador(k)))))

            cambioDados = input("indique si quiere cambiar dados S").upper()

            if cambioDados == "S":
                nDadosCambiar = t.leer_entero("cuantos dados quieres cambiar")
            print(player.dados_jugador.cambiar_dados(nDadosCambiar))

            opcion = m.Menu.gestionar()
            if opcion == 1:
                print(p.Partida.risco(player))

            elif opcion == 2:
                print(p.Partida.trece(player))

            elif opcion == 3:
                print(p.Partida.escalera_mayor(player))

            elif opcion == 4:
                print(p.Partida.escalera_menor(player))

            elif opcion == 5:
                print(p.Partida.escalera_par(player))

            elif opcion == 6:
                print(p.Partida.escalera_impar(player))

            elif opcion == 7:
                print(p.Partida.trio(player))

            elif opcion == 8:
                print(p.Partida.numero(player, 6))

            elif opcion == 9:
                print(p.Partida.numero(player, 5))

            elif opcion == 10:
                print(p.Ppartida.numero(player, 4))

            elif opcion == 11:
                print(p.Partida.numero(player, 3))

            elif opcion == 12:
                print(p.Partida.numero(player, 2))

            elif opcion == 13:
                print(p.Partida.numero(player, 1))

            else:
                print("opcion no valida")
                k -= 1

            p.Partida.muestraTablero()

            exporto = input("\nPulsa Intro para seguir o e para exportar tus datos actuales[Intro/e]: ")

            if exporto == "E":
                player.guarda_datos()
