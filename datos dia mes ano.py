

class Data:
    def __init__(self,dia,mes,ano):
        self.setDia(dia)
        self.setMes(mes)
        self.setAno(ano)

    def setAno(self,ano):
        if type(ano) == int:
            if ano > 0:
                self.__ano = ano
                return self.__ano
            else:
                self.__ano = 0
                return self.__ano

    def setMes(self,mes):
        if type(mes) == int:
            if mes > 0 and mes< 13:
                self.__mes = mes
                return self.__mes
            else:

                self.__mes = 0
                return self.__mes


    def setDia(self, dia):
        if type(dia) == int:
            if dia > 0 and dia < 32:
                self.__dia = dia
                return self.__dia
            else:
                self.__dia = 0
                return self.__dia

    def setComprobar(self,dia,mes,ano):
        if type(dia) == 0 or type(mes) == 0 or type(ano) == 0:
            self.__dia = 0
            self.__mes = 0
            self.__ano = 0
        if mes == 2:
            if dia< 28 or dia>0:
                self.__dia = 0
                self.__mes = 0
                self.__ano = 0
        return self.__dia, self.__mes, self.__ano
    def getAno(self):
        return self.__ano

    def getMes(self):
        return self.__mes

    def getDia(self):
        return self.__dia
    def getComprobar(self):
        return set.__dia, set.__mes, set.__ano

    def aCadea(self):
        cadeaData= "Horario: \n\t dia= "+ str(self.__dia) + "\n\t mes = "+ str(self.__mes) + "\n\t ano = "+ str(self.__ano)
        return cadeaData


data = Data(30,2,2001)
print(data.aCadea())
data.dia = 42
print (data.dia)

