class Horario:
    def __init__(self,horas = 0, *minutoSegundo):
       if isinstance (horas,int):
           self.__asignacionHoraInt(horas,minutoSegundo)
       if type(horas) == str:
           self.__asignacionHoraStr(horas)
       if type(horas) == list:
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

    def setHoras(self,horas):
        if horas<24 and horas >= 0:
            return horas
        else:
            horas = None
            return horas

    def getHoras(self):
        return self.__horas
    def setMinutos(self,minutos):
        if minutos<24 and minutos >= 0:
            return minutos
        else:
            minutos = None
            return minutos


    def getMinutos(self):
        return self.__minutos
    def setSegundos(self,segundos):
        if segundos<24 and segundos >= 0:

            return segundos
        else:
            segundos = None
            return segundos
    def getSegundos(self):
        return self.__segundos

    def aCadea(self):
            cadea = "\n\t horas : " + str(self.__horas) + "\n\t minutos: " + str(
                self.__minutos) + "\n\t segundos: " + str(self.__segundos)
            return cadea


 horario = Horario(5, 44)

print( horario.aCadea())