 -*- coding: utf-8 -*-
import utiles.Menu as m
import utiles.Teclado as t
import dados.Partida as p
import dados.Jugador as j

if __name__ == "__main__":
    opciones = "Risco", "Trece", "Escalera Mayor", "Escalera Menor ", "Escalera par", "Escalera impar", "Trio", "Seis", \
               "Cinco", "Cuatro", "Tres", "Dos", "Ases "
    menu = m.Menu("Indique la opción que quiere realizar:", opciones)

    nJugadores = t.leer_entero("Indica cuantos jugadores sois: ")

    partida = p.Partida(nJugadores)

    for i in range(0, nJugadores):
        nombre_tmp = input("Introduce el nombre del jugador: ")
        partida.crear_jugadores(i, nombre_tmp)

    for i in range(14):
        for k in range(nJugadores):
            player = partida.jugadores[partida.jugadores.index(j.Jugador(k))]

            print(f"\nTurno {str(i)} del jugador {partida.jugadores[partida.jugadores.index(j.Jugador(k))].nombre}")

            print(f"\nEn esta tirada obtienes: \n"
                  f"{partida.tirar_dados(partida.jugadores[partida.jugadores.index(j.Jugador(k))])}")

            cambio_dados = input("\n¿Quieres cambiar algún dado? [S/N]: ").upper()

            if cambio_dados == "S":
                ndados_cambiar = t.leer_entero("¿Cuántos dados quieres cambiar? ")
                print(player.dados_jugador.cambiar_dados(ndados_cambiar))

            # Inicializo casilla_ocupada como si no lo estuviera
            # para que entre al bucle
            casilla_ocupada = True
            while casilla_ocupada:
                opcion = menu.gestionar()

                if opcion == 1:
                    juegoencurso = partida.risco(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Risco: 50 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 2:
                    juegoencurso = partida.trece(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Trece: 26 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 3:
                    juegoencurso = partida.escalera_mayor(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Escalera Mayor: 20 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 4:
                    juegoencurso = partida.escalera_menor(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Escalera Menor: 20 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 5:
                    juegoencurso = partida.escalera_par(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Escalera Par: 20 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 6:
                    juegoencurso = partida.escalera_impar(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Escalera Impar: 20 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 7:
                    juegoencurso = partida.trio(player)
                    if juegoencurso == 0:
                        print("Ha obtenido 0 puntos.")
                        casilla_ocupada = False
                    elif juegoencurso == 1:
                        print("Has completado la casilla Escalera Trío: 25 puntos.")
                        casilla_ocupada = False
                    else:
                        print("Casilla ocupada, indique una casilla vacía.")

                elif opcion == 8:
                    juegoencurso = partida.numero(player, 6)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla seises completada con " + juegoencurso)

                elif opcion == 9:
                    juegoencurso = partida.numero(player, 5)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla cincos completada con " + juegoencurso)

                elif opcion == 10:
                    juegoencurso = partida.numero(player, 4)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla cuatros completada con " + juegoencurso)

                elif opcion == 11:
                    juegoencurso = partida.numero(player, 3)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla treses completada con " + juegoencurso)

                elif opcion == 12:
                    juegoencurso = partida.numero(player, 2)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla doses completada con " + juegoencurso)

                elif opcion == 13:
                    juegoencurso = partida.numero(player, 1)
                    if juegoencurso == 50:
                        print("Casilla ocupada, indique una casilla vacía.")
                    else:
                        print("Casilla ases completada con " + juegoencurso)

                else:
                    print("Opción no válida")
                    k -= 1

            partida.muestra_tablero()

            exporto = input("\nPulsa Intro para seguir o e para exportar tus datos actuales[Intro/e]: ").upper()

            if exporto == "E":
                player.crea_archivo()
            else:
                print("")