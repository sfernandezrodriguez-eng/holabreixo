
class Horario:
    def __init__(self,horas = 0, *minutoSegundo):
       if isinstance (horas,int):
           self.__asignacionHoraInt(horas,minutoSegundo)
       if type(horas) == str:
           self.__asignacionHoraStr(horas)

       if type(horas) == float:
           self.__asignacionHoraFloat(horas)

    def __asignacionHoraInt(self,horas, minutoSegundo):
        self.setHoras(horas)
        if minutoSegundo is not None:
            if len(minutoSegundo) == 1:
                if isinstance(minutoSegundo[0], int):
                    self.setMinutos(minutoSegundo[0])
            elif len(minutoSegundo) == 2:
                if isinstance(minutoSegundo[0], int):
                    self.setMinutos(minutoSegundo[0])
                if isinstance(minutoSegundo[1], int):
                    self.setSegundos(minutoSegundo[1])

    def __asignacionHoraStr(self, horas):
         if len(horas) == 8:
            if horas[2] == ':' and horas[5] == ':':
                hms = horas.split(':')

                if hms[0].isnumeric:
                    h = int(hms[0])
                    if h<24 and h>=0:
                        self.setHoras(h)
                if hms[1].isnumeric:
                    m = int(hms[1])
                    if m<60 and m>=0:
                        self.setMinutos(m)
                if hms[2].isnumeric:
                    s = int(hms[2])
                    if s<60 and s>=0:
                        self.setSegundos(s)
            return  h,m,s

    def __asignacionHoraColection(self, horas):
        if isinstance (horas,list) or isinstance(horas,tuple):
            if len (horas) == 3:
               if isinstance (horas[0],int):
                        if horas[0]<24 and horas[0]>=0:
                            self.setHoras(horas[0])
               if isinstance (horas[1],int):
                   if horas[1] < 60 and horas[1] >= 0:
                       self.setMinutos(horas[1])
               if isinstance (horas[2],int):
                   if horas[2] < 24 and horas[2] >= 0:
                        self.setSegundos(horas[2])

               else:
                    horas = None
                    return horas
            if len (horas) == 2:
               if isinstance (horas[0],int):
                        if horas[0]<24 and horas[0]>=0:
                            self.setHoras(horas[0])
               if isinstance (horas[1],int):
                   if horas[1] < 60 and horas[1] >= 0:
                       self.setMinutos(horas[1])
                       self.setSegundos(0)
            if len (horas) == 1:
               if isinstance (horas[0],int):
                        if horas[0]<24 and horas[0]>=0:
                            self.setHoras(horas[0])
                            self.setMinutos(0)
                            self.setSegundos(0)

    def __asignacionHoraFloat(self, horas):
        if isinstance (horas,float):
            if horas<24:
               resto1 = horas%1
               minutos = resto1 * 60
               resto3 = minutos%1

               s = resto3 * 60
               self.setHoras(int(horas))
               self.setMinutos(int(minutos))
               self.setSegundos(int(s))
            else:
                self.setHoras(0)
                self.setMinutos(0)
                self.setSegundos(0)
        else:
            self.setHoras(0)
            self.setMinutos(0)
            self.setSegundos(0)

    def setHoras(self,horas):
        if horas<24 and horas >= 0:
            return horas
        else:
            horas = None
            return horas

    def getHoras(self):
        return self.horas
    def setMinutos(self,minutos):
        if minutos<24 and minutos >= 0:
            return minutos
        else:
            minutos = None
            return minutos


    def getMinutos(self):
        return self.minutos
    def setSegundos(self,segundos):
        if segundos<24 and segundos >= 0:

            return segundos
        else:
            segundos = None
            return segundos
    def getSegundos(self):
        return self.segundos
    def converterMinutos(self,minutos,horas):
        if type(minutos) > 60:
            horas = horas + 1
            minutos = minutos - 60

            return horas and minutos
        else:
            return minutos
    def converterSegundos(self,segundos,minutos):
        if type(segundos) > 60:
            self.minutos = minutos + 1
            self.segundos = segundos - 60
            return self.segundos and self.minutos
        else:
            return self.segundos
    def incrementarHoras(self,horas):

        minutos = (horas % 1) *  60
        self.incrementarMinutos(minutos)
        horas = int(horas//1)
        self.__horas = (self.__horas + horas) % 24

    def incrementarMinutos(self, minutos):

        segundos = int((minutos%1)*60)
        self.incrementarSegundos(segundos)
        minutos = int((minutos//1))
        horas= minutos // 60
        minutos = minutos-60*horas
        self.incrementarHoras(horas)
        self.__minutos = self.__minutos + minutos
        if self.__minutos >= 60:
            self.__minutos = self.__minutos % 60
            self.incrementarHoras(1)

    def incrementarSegundos(self, segundos):

        minutos = segundos // 60
        self.incrementarMinutos(minutos)
        segundos = self.__segundos - minutos * 60
        self.__segundos = self.__segundos + segundos
        if self.__segundos >= 60:
            self.__segundos = self.__segundos % 60
            self.__minutos += 1
            if self.__minutos >= 60:
                self.__minutos = self.__minutos % 60
                self.__horas +=1

    def mostrarFormato12H(self,horas):
        if self.__horas>= 13:
            self.__horas = self.__horas - 12
        return self.__horas
    def aCadea(self):
        cadea ="\n\t horas : " + str(self.__horas) + "\n\t minutos: " + str(self.__minutos)+ "\n\t segundos: " + str(self.__segundos)
        return cadea

horario = Horario(5,44)
print( horario.aCadea())