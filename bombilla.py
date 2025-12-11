

class Bombilla:
    def __init__(self,pulso):
        self.setBombilla(pulso)
    def setBombilla(self,pulso):
        if pulso < 2 or pulso > -1:
            if pulso == 0:
                self.pulso= False
                return self.pulso
            else:
                self.pulso=True
            return self.pulso
    def getBombilla(self,pulso):
       return self.setBombilla(pulso)
    def Enciende(self,pulso):
        if pulso == 1:
            self.pulso = True
            return self.pulso
        else:
            self.pulso = False
            return self.pulso
    def Apaga(self,pulso):
        if pulso == 0:
            self.pulso = False
            return self.pulso
        else:
            self.pulso = True
            return self.pulso
    def Estado(self):
        return self.pulso

    def aCadea(self,pulso):
        cadeaBombilla=str(self.pulso)
        return cadeaBombilla


bombilla= Bombilla(0)
print(bombilla.Apaga(0),bombilla.Enciende(1),bombilla.Estado())