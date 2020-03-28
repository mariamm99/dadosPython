# -*- coding: utf-8 -*-
import utiles.Menu as m
import utiles.Teclado as t
import dados.Partida as p
import dados.Jugador as j

opciones = "Risco", "Trece", "Escalera Mayor", "Escalera Menor ", "Escalera par", "Escalera impar", "Trio", "Seis", \
           "Cinco", "Cuatro", "Tres", "Dos", "Ases "
menu = m.Menu("Indique la opción que quiere realizar:", opciones)

nJugadores = t.leer_entero("Indica cuantos jugadores sois: ")

partida = p.Partida(nJugadores)

for i in range(0, nJugadores):
    nombre_tmp = input("Introduce el nombre del jugador: ")
    partida.crear_jugadores(i, nombre_tmp)

for i in range(1, 14):
    for k in range(0, nJugadores):
        player = partida.jugadores[partida.jugadores.index(j.Jugador(k))]

        print(f"\nTurno {str(i)} del jugador {partida.jugadores[partida.jugadores.index(j.Jugador(k))].nombre}")

        print(f"\nEn esta tirada obtienes: \n"
              f"{partida.tirar_dados(partida.jugadores[partida.jugadores.index(j.Jugador(k))])}")

        cambio_dados = input("\n¿Quieres cambiar algún dado? [S/N]: ").upper()

        if cambio_dados == "S":
            ndados_cambiar = t.leer_entero("cuantos dados quieres cambiar")
            print(player.dados_jugador.cambiar_dados(ndados_cambiar))

        opcion = menu.gestionar()
        if opcion == 1:
            print(partida.risco(player))

        elif opcion == 2:
            print(partida.trece(player))

        elif opcion == 3:
            print(partida.escalera_mayor(player))

        elif opcion == 4:
            print(partida.escalera_menor(player))

        elif opcion == 5:
            print(partida.escalera_par(player))

        elif opcion == 6:
            print(partida.escalera_impar(player))

        elif opcion == 7:
            print(partida.trio(player))

        elif opcion == 8:
            print(partida.numero(player, 6))

        elif opcion == 9:
            print(partida.numero(player, 5))

        elif opcion == 10:
            print(partida.numero(player, 4))

        elif opcion == 11:
            print(partida.numero(player, 3))

        elif opcion == 12:
            print(partida.numero(player, 2))

        elif opcion == 13:
            print(partida.numero(player, 1))

        else:
            print("Opción no válida")
            k -= 1

        partida.muestra_tablero()

        exporto = input("\nPulsa Intro para seguir o e para exportar tus datos actuales[Intro/e]: ")

        if exporto == "E":
            player.guarda_datos()
