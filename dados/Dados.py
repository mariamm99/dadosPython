import math

class Dados:

    def __init__(self):

        self.setD1()
        self.setD2()
        self.setD3()

    def getD1(self):
        return self.d1

    def setD1(self):
        self.d1= int( math.random()* 6+1)

    def getD2(self):
        return self.d2

    def setD2(self):
        self.d2 = int(math.random() * 6 + 1)

    def getD3(self):
        return self.d3

    def setD3(self):
        self.d3 = int(math.random() * 6 + 1)

    def __str__(self):
        return "Dado 1: " + self.getD1() + "\nDado 2: " + self.getD2() + "\nDado 3: " + self.getD3();

    def cambiarDados(self, nDadosCamibar):
        if nDadosCamibar>2:
            if nDadosCamibar>3:
                print("solo puedes cambiar 3 dados, se cambiaran los 3")
            self.setD1()
            self.setD2()
            self.setD3()

            return str()

        cambiod1=True
        cambiod2=True
        cambiod3=True

        for i in range(0, nDadosCamibar):
            i+=1
            dado=int(input("indique que dado quiere cambiar, 1 , 2 o 3"))
            if dado ==1 and cambiod1:
                self.setD1()
                cambiod1=False
            elif dado == 2 and cambiod2:
                self.setD2()
                cambiod2=False
            elif dado==3 and cambiod3:
                self.setD3()
                cambiod3=False

            elif cambiod3==False or cambiod2==False or cambiod1==False:
                print("Dado " + dado + " ya ha sido cambiado introduzca otro")
                i-=1

            else:
                print("Dado " + dado + " no existe introduzca otro")
                i-=1



