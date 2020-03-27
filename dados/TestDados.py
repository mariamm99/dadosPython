# -*- coding: utf-8 -*-
import utiles.Menu as m
import utiles.Teclado as t
import dados.Partida as p
from dados import Partida
import dados.Jugador as j


class TestPartida:
    opciones = "Risco", "Trece", "Escalera Mayor", "Escalera Menor ", "Escalera par", "Escalera impar", "Trio", "Seis", "Cinco", "Cuatro", "Tres", "Dos", "Ases"
    menu= m.Menu("Indique la opción que quiere realizar:", opciones)

if __name__ == "__main__":
    nJugadores=t.leer_entero("Indica cuantos jugadores sois: ")

    partida = p.partida(nJugadores)

    for i in range(0, nJugadores):
        nombreTmp=input("Introduce el nombre del jugador")
        partida.crearJugadores(i,nombreTmp)
        i+=1

    for i in range(1,13):
        for k in range(1, nJugadores):
            k+=1
            player = j.Jugador.

            print("\n Turno " + i + "del jugador" +(partida.jugadores.indexOf(j.Jugador(k ))).getNombre())

            print("\nEn esta tirada obtienes:\n"
						+ Partida.tirarDados(partida.jugadores.get(partida.jugadores.indexOf(j.Jugador(k)))))

            cambioDados=input("indique si quiere cambiar dados S").upper()

            if cambioDados=="S":
                nDadosCambiar= t.leer_entero("cuantos dados quieres cambiar")
                print(player.dados_jugador.cambiarDados(nDadosCambiar))

            opcion= m.Menu.gestionar()
            if opcion==1:
                print(partida.Risco())

            elif opcion ==2:
                print(partida.Trece())

            elif opcion==3:
                print(partida.EscaleraMayor())

            elif opcion == 4:
                print(partida.EscaleraMenor())

            elif opcion == 5:
                print(partida.EscaleraPar())

            elif opcion == 6:
                print(partida.EscaleraImpar())

            elif opcion == 7:
                print(partida.Trio())

            elif opcion == 8:
                print(partida.numero(player, 6))

            elif opcion == 9:
                print(partida.numero(player,5))

            elif opcion == 10:
                print(partida.numero(player, 4))

            elif opcion == 11:
                print(partida.numero(player,3))

            elif opcion == 12:
                print(partida.numero(player,2))

            elif opcion == 13:
                print(partida.numero(player,1))

            else:
                print("opcion no valida")
                j-=1

    partida.muestraTablero()

    exporto=input("\nPulsa Intro para seguir o e para exportar tus datos actuales[Intro/e]: ")

    if exporto=="E":
        player.guarda_datos()

