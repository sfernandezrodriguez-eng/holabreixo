


class Horario:
    def __init__(self,horas,minutos,segundos):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
    def setHoras(self,horas):
        if horas== int() and horas >= 0:
            return horas
        else:
            horas = None
            return horas

    def getHoras(self):
        return self.horas
    def setMinutos(self,minutos):
        if minutos== int() and minutos >= 0:

                return minutos
        else:
            minutos = None
            return minutos


    def getMinutos(self):
        return self.minutos
    def setSegundos(self,segundos):
        if segundos == int() and segundos >= 0:

                return segundos
        else:
            segundos = None
            return segundos
    def getSegundos(self):
        return self.segundos
    def converterMinutos(self,minutos,horas):
        if minutos > 60:
            horas = horas + 1
            minutos = minutos - 60

            return horas and minutos
        else:
            return minutos
    def converterSegundos(self,segundos,minutos):
        if segundos > 60:
            minutos = minutos + 1
            segundos = segundos - 60

            return segundos and minutos
        else:
            return segundos
    def incrementarHoras(self,horas):
        cambio =int(input("cuantas horas añades:"))
        self.horas = horas + cambio
        return self.horas
    def incrementarMinutos(self, minutos):
        cambio = int(input("cuantas minutos añades:"))
        self.minutos = minutos + cambio
        return self.minutos
    def incrementarSegundos(self, segundos):
        cambio = int(input("cuantas segundos añades:"))
        self.segundos = segundos + cambio
        return self.segundos
    def mostrarFormato12H(self,horas):
        if horas>= 13:
            self.horas = horas - 12
        return self.horas
    def aCadea(self):
        cadea ="\n\t horas : " + str(self.horas) + "\n\t minutos: " + str(self.minutos)+ "\n\t segundos: " + str(self.segundos)
        return cadea

horario = Horario(13,44,56)
print(horario.incrementarHoras(13),horario.aCadea())