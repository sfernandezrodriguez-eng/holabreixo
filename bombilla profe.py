class Bombilla:
    def __init__(self):
        self.__estado=False
        self.__interruptorXeral= True
    def estaAcendida(self):
        if Bombilla.interruptorXeral == True:
            self.__estado = True
        return self.__estado and Bombilla.interruptorXeral

    def acende(self):
        self.__estado = True

    def apaga(self):
        self.__estado = False

    def conmuta(self):
        self.__estado = not self.__estado
        return self.__estado

    def comrpobarEstado(self):
        return self.__estado

    def __str__(self):
        return "A bombilla esta acendida" if self.__estado and Bombilla.interruptorXeral else "A bombilla esta apagada"


b1 = Bombilla()
b2 = Bombilla()
Bombilla.interruptorXeral = True
b1.estaAcendida()
print(b1.interruptorXeral,)
print(b1)

